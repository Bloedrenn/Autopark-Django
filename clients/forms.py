from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Client
from AutoparkProject.settings import DATE_INPUT_FORMATS


class UserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ('username', 'password1', 'password2', 'email') # Атрибуты будут взяты из UserCreationForm

        labels = {
            'username': 'Логин',
            'email': 'Электронная почта'
        }

        help_texts = {
            'username': ''
        }


class ClientForm(forms.ModelForm):
    birthday = forms.DateField(label='Дата рождения', input_formats=DATE_INPUT_FORMATS)

    class Meta:
        model = Client

        exclude = ['user']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
