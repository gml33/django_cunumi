from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import *

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model=Usuario
        fields='__all__'

#login user
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = '__all__'



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


class evolucionForm(forms.ModelForm):

    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = evolucion
        fields = '__all__'


class derivacionForm(forms.ModelForm):

    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = derivacion
        fields = '__all__'


class historiaClinicaForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = historiaClinica
        fields = '__all__'

class facturaForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = factura
        fields = '__all__'

class pagoForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = pago
        fields = '__all__'

class turnoForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = turno
        fields = '__all__'

class informeForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = informe
        fields = '__all__'