from django import forms
from hands.models import Hands_info

class Profile_form(forms.ModelForm):
    class Meta:
        model = Hands_info        
        fields = (
            'name',
            'description',
            'contact',
            'rate_per_day',
            'skills',
            'portrait',
        )