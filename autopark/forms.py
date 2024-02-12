import datetime
from django import forms

from .models import Driver
from AutoparkProject.settings import DATE_INPUT_FORMATS


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver

        exclude = ['is_available']
