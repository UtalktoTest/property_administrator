from django.urls import  path

from .views import CommunicationsAPI, communication_feed, messages_details

urlpatterns = [
    
    path('feed/<str:token>', communication_feed, name='communication_feed'),
    path('messages-details/<int:tenant_id>/<str:token>', messages_details, name='messages_details' ),
    
    
    # API PART -------------------------------------
    
    path('send-message/', CommunicationsAPI.as_view()),
  

]