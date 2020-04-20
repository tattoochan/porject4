from django.db import models
from accounts.models import MyUser

# Create your models here.
class Job_detail (models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE,
        null= False,
        blank = False
        )
    position = models.CharField(
        max_length = 32,
        blank = False,
        )
    description = models.TextField(
        max_length = 256,
        blank = False,
        )
    contact = models.IntegerField (
        blank = False,
        )    
    rate_per_day = models.IntegerField(
        blank = False,
        default = 20
        )
        
    def __str__(self):
        return (self.job_name)