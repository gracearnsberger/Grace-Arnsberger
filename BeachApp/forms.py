from django.forms import ModelForm, DateInput
from .models import savecities
from django import forms

#form for save cities page
class DateInput(forms.DateInput):
    input_type = 'date'

class CityForm(ModelForm):
    class Meta:
        model = savecities
        fields = '__all__'
        widgets = {
            'date_saved': DateInput()
        }