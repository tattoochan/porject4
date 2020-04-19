from django import forms
from tasks.models import Job_detail

class Job_form(forms.ModelForm):
    class Meta:
        model = Job_detail        
        fields = (
            'position',
            'description',
            'contact',
            'rate_per_day',
        )