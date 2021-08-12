from django import forms
from .models import *
  
class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ['event_name', 'event_image', 'date', 'time', 'address_line', 'city', 'state', 'zipcode']