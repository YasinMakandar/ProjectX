from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from django import *

from django import forms
from .models import Record

from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields  = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CreateRecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields  = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']


class UpdateRecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields  = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']

