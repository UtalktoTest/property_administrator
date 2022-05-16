# python 

import datetime

# django

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status

# models 

from .models import Ticket, TicketPriority, TicketType, MaintanenceType, MaintanenceIssueType, MaintanenceSubIssueType, MaintanenceIssueDescription, TicketAction, TicketStatus
from .serializers import TicketSerializer, TicketTypeSerializer, TicketPrioritySerializer

# properties
from properties.models import Properties, Tenants, Units
from properties.serializers import UnitsSerializer, TenantSerializer

# Create your views here.

# It is possible to create more nodes if in the future the app would allow to add more ticket types



def home(request):
    
    tickets_open = Ticket.objects.filter(date_closed__isnull=True)
    
    maintenance_tickets = Ticket.objects.filter(ticket_type=1).count()
    payment_tickets = Ticket.objects.filter(ticket_type=2).count()
    general_info_tickets = Ticket.objects.filter(ticket_type=3).count()
    
    return render(
        request, 
        'tickets/main_pages/dashboard-main.html', 
        {
            
            'tickets_open': tickets_open, 
            
            'quantity_tickets_open': tickets_open.count(),
            'maintenance_tickets': maintenance_tickets,
            'payment_tickets': payment_tickets,
            'general_info_tickets': general_info_tickets,
        })


def create_ticket_main_info(request):
    
    next_stage = request.GET.get('next_stage')

    
    if next_stage == '1':
        
        units = UnitsSerializer(Units.objects.filter(property=int(request.GET.get('option_id'))), many=True)
        return JsonResponse({'options': units.data, 'stage_title': 'Select Unit', 'next_stage': 2} )
    
    elif next_stage == '2':
        
        tenants = TenantSerializer(Tenants.objects.filter(unit=int(request.GET.get('option_id'))), many=True)
        return JsonResponse( {'options': tenants.data, 'stage_title': 'Select Tenant', 'next_stage': 3} )
    
    
    elif next_stage == '3':
        
        tickets = TicketTypeSerializer(TicketType.objects.all(), many=True)
        return JsonResponse( {'options': tickets.data, 'stage_title': 'Select Type of issue', 'next_stage': 4} )
    
    elif next_stage == '4':
        priorities = TicketPrioritySerializer(TicketPriority.objects.all(), many=True)
        return JsonResponse( {'options':  priorities.data, 'next_stage': 5})
    
    
    elif next_stage == '5':
        
        ### start ticket creation ###
        tenant_id = int(request.GET.get('tenant_id'))
        ticket_priority = int(request.GET.get('option_id'))
        data = {
            'created_by': tenant_id,
            'ticket_type': int(request.GET.get('ticket_type')),
            'unit': Tenants.objects.get(id=tenant_id).unit.id,
            'date_opened' : datetime.datetime.now(),
            'priority': ticket_priority,
            'ticket_status': 1,
        }
        
        serializer = TicketSerializer(data=data)
        
        if serializer.is_valid():
            print(data)
            serializer.save()
            return JsonResponse( {'message': 'created'})
        else:
            return JsonResponse(
                {
                    'message': 'serializer is not valid', 
                    'serializer_error': serializer.errors
                }, 
                status=status.HTTP_400_BAD_REQUEST
                )
        
        
        

    properties = Properties.objects.all()
    
    return render(
        request,
        'tickets/main_pages/create-ticket-dashboard.html',
        {
            'properties': properties, 
        })


def create_ticket_options(request, ticket_type:int, tenant_id:int):
    
    if ticket_type == 1:
        fields = MaintanenceType.objects.all()
        
    form_fields = {}

    for i, _field in enumerate(list(fields)):
        form_fields[f'field{i}'] = {
            'id': _field.id,
            'string': _field.string_part
        }
        

    return render( 
        request,
        'tickets/main_pages/create-ticket-options.html', 
        {
            'form_fields': form_fields, 
            'branch_selected': ticket_type, 
            'tenant_id':tenant_id
        })


def ticket_info(request, ticket_id):
    ticket = Ticket.objects.get(id=int(ticket_id))
    ticket_statuses = TicketStatus.objects.filter(ticket_type=ticket.ticket_type.id).order_by('id')
    
    # here the link to identify the problem must be sent with the ticket id 
        
        
    current_status = ticket_statuses[ticket.ticket_status.id]
    
    
    return render(
        request, 
        'tickets/main_pages/view-ticket-detail.html',
        {
            'ticket': ticket,
            'ticket_statuses': ticket_statuses,
            'current_status' : current_status,
        }
        )


# JSON RESPONSES --------------------------------------------

def ticket_tree_stage_info(request): 
    
    branch_selected = int(request.POST.get('branch_selected'))
    stage_status = int(request.POST.get('next_stage'))
    option_selected = int(request.POST.get('option_selected'))
    

    # branch with id '1' is for maintanance
    if branch_selected == 1:
        
        # this will return the initial options <<maintanence_type>>
        if stage_status == 2:
            fields = MaintanenceIssueType.objects.filter(maintanence_type=option_selected)
            stage_title = 'Maintanence Issue'
        
        elif stage_status == 3:
            fields = MaintanenceSubIssueType.objects.filter(maintanence_issue_type=option_selected)
            stage_title = 'Sub Maintanence Issue'
            
        elif stage_status == 4:
            fields = MaintanenceIssueDescription.objects.filter(maintanence_issue_sub_type=option_selected)
            stage_title = 'Maintanence Issue Description'
        
        elif stage_status == 5:
            fields = TicketAction.objects.filter(issue_description=option_selected)
            stage_title = 'Action to do'
            
    
    form_fields = {}

    for i, _field in enumerate(list(fields)):
        form_fields[f'field{i}'] = {
            'id': _field.id,
            'string': _field.string_part
        }
        
    return JsonResponse({
        'form_fields': form_fields,
        'stage_title': stage_title,
        'current_stage' : stage_status + 1,
        'branch_selected' : branch_selected
        })
