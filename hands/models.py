from django.db import models
from accounts.models import MyUser

# Create your models here.
class Hands_info (models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE,
        null= False,
        blank = False
        )
    
    name = models.CharField(
        max_length = 64,
        blank = False,
        # default = "No information"
        )
    
    description = models.TextField(
        max_length = 256,
        blank = False,
        # default = "No info available"
        )
        
    contact = models.IntegerField (
        blank = False,
        )    
    
    rate_per_day = models.IntegerField(
        blank = False,
        default = 20
        )
    
    SKILLS = [
        ('Tutoring', 'Tutoring'),
        ('Gardening', 'Gardening'),
        ('Cleaning', 'Cleaning'),
        ('Delivery', 'Delivery'),
        ('Tele-calling','Tele-calling'),
        ('Others','Others'),
        ]
    
    skills = models.CharField(
        max_length = 16,
        choices = SKILLS,
        default = 'Others')
        
    
    def __str__(self):
        return (self.hand_name)