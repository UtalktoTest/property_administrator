from django.db import models

from register.models import CustomUser
from properties.models import Units


class Candidate(models.Model):
    # foreign keys
    
    property_manager = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE, default=0)
    unit = models.ForeignKey(Units, null=False, blank=False ,on_delete=models.CASCADE, default=0)
    
    # ---------------------------------
    # fields
    
    availability_date = models.JSONField(null=False) 
    adults_information = models.JSONField(null=False) # there can be more than one adult 
    appointment = models.DateTimeField()
    
    current_address = models.CharField(max_length=400, null=False)
    current_landlord_name = models.CharField(max_length=100, null=False)
    current_landlord_phone = models.CharField(max_length=100, null=False)
    
    duratin_of_lease = models.CharField(max_length=25, null=False)
    
    expected_renting_duration = models.IntegerField(null=False)
    
    family_income = models.DecimalField(max_digits=19, decimal_places=2, null=False)
    
    length_of_time_at_current_address = models.CharField(max_length=400)
        
    number_of_adults = models.IntegerField(null=False)
    number_of_children = models.IntegerField(null=False)

    will_be_pets = models.BooleanField(null=False)
    pets = models.JSONField()

    previous_unit_time = models.CharField(max_length=255)
    preferred_move_in_date = models.DateField(null=False)

    reason_for_moving = models.TextField(null=False)
    relevant_information = models.TextField(null=False)
    
    score = models.IntegerField()
    max_score = models.IntegerField()
    
    
    def __str__(self) -> str:
        return str(self.score)
    
