from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import *

#register/create a user

class CreateUserForm(UserCreationForm):
    
    class Meta:

        model=User
        fields=['username', 'first_name', 'last_name','email','password1', 'password2']

#login user
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())



class pacienteForm(forms.ModelForm):
    estado_choices = (
        ('activo', 'activo'),
        ('inactivo', 'inactivo'),
        ('alta', 'alta'),
        ('derivado', 'derivado')
    )
    estado = forms.ChoiceField(
        choices=estado_choices, widget=forms.RadioSelect())
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model=paciente
        fields = '__all__'



class modificarPacienteForm(forms.ModelForm):

    class Meta:
        model = paciente
        fields = '__all__'