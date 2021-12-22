from django import forms
from .models import Passenger,User
from django.forms.models import inlineformset_factory

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = [
            'first_name', 
            'last_name', 
            'gender'
        ]

PassengerFormSet = inlineformset_factory(
    User,
    Passenger,
    PassengerForm,
    can_delete=False,
    min_num=0,
    extra=0
)