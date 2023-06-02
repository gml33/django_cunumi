from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, pacienteForm, modificarPacienteForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .bot import bot, chat_id
from .models import paciente

def home(request):
    return render(request, 'webapp/index.html')

#register view

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context={'form':form}
    return render(request, 'webapp/register.html', context=context)

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                #bot.send_message(chat_id, text='Logueado')
                return redirect('dashboard')
    context = {'form':form}
    return render(request, 'webapp/my-login.html', context=context)

@login_required(login_url='my-login')
def dashboard(request):
    pacientes = paciente.objects.all().order_by('-id')
    context = {
        'pacientes':pacientes,
    }
    return render(request, 'webapp/dashboard.html', context=context)

#agregar paciente

@login_required(login_url='my-login')
def agregar_paciente(request):
    form = pacienteForm()
    if request.method == 'POST':
        form = pacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request, 'webapp/create.html', context=context)

#modificar paciente

@login_required(login_url='my-login')
def modificar_paciente(request, pk):
    paciente_seleccionado = paciente.objects.get(id=pk)
    form = modificarPacienteForm(instance=paciente_seleccionado)
    if request.method == 'POST':
        form = modificarPacienteForm(request.POST, instance=paciente_seleccionado)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request, 'webapp/update.html', context=context)

#detalle paciente

@login_required(login_url='my-login')
def detalle_paciente(request, pk):
    paciente_seleccionado = paciente.objects.get(id=pk)    
    context = {
        'paciente':paciente_seleccionado
    }
    return render(request, 'webapp/view.html', context=context)

@login_required(login_url='my-login')
def eliminar_paciente(request, pk):
    paciente_seleccionado= paciente.objects.get(id=pk)
    paciente_seleccionado.delete()
    return redirect('dashboard')


def user_logout(request):
    auth.logout(request)
    return redirect('my-login')