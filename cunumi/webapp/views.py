from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, pacienteForm, pacienteForm, historiaClinicaForm, evolucionForm, derivacionForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .bot import bot, chat_id
from .models import paciente,historiaClinica, evolucion, derivacion
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User

def home(request):
    return render(request, 'registro/index.html')

#register view

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context={'form':form}
    return render(request, 'registro/register.html', context=context)

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
    return render(request, 'registro/my-login.html', context=context)

@login_required(login_url='my-login')
def dashboard(request):
    pacientes = paciente.objects.all().order_by('-id')
    context = {
        'pacientes':pacientes,
    }
    return render(request, 'webapp/dashboard.html', context=context)

def user_logout(request):
    auth.logout(request)
    return redirect('my-login')
#----------------------------Pacientes-------------------------------

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
    return render(request, 'webapp/paciente/agrgar.html', context=context)

@login_required(login_url='my-login')
def eliminar_paciente(request, pk):
    paciente_seleccionado= paciente.objects.get(id=pk)
    paciente_seleccionado.delete()
    return redirect('dashboard')

@login_required(login_url='my-login')
def modificar_paciente(request, pk):
    paciente_seleccionado = paciente.objects.get(id=pk)
    form = pacienteForm(instance=paciente_seleccionado)
    if request.method == 'POST':
        form = pacienteForm(request.POST, instance=paciente_seleccionado)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request, 'webapp/paciente/modificar.html', context=context)

@login_required(login_url='my-login')
def detalle_paciente(request, pk):
    paciente_seleccionado = paciente.objects.get(id=pk)    
    context = {
        'paciente':paciente_seleccionado
    }
    return render(request, 'webapp/paciente/detalle.html', context=context)

# ------------historiaClinicas-------------------------------------------
@permission_required('webapp.add_historiaClinica')
def agregar_historiaClinica(request):
    data = {
        'form': historiaClinicaForm()
    }
    if request.method == 'POST':
        formulario = historiaClinicaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "historiaClinica agregada correctamente")
            return redirect(to="webapp:listar_historiaClinicas")
        else:
            data["form"] = formulario
    return render(request, 'webapp/historiaClinica/agregar.html', data)


@permission_required('webapp.view_historiaClinica')
def listar_historiaClinicas(request):
    historiaClinicas = historiaClinica.objects.all().order_by('fecha')
    data = {
        'historiaClinicas': historiaClinicas
    }
    return render(request, 'webapp/historiaClinica/listar.html', data)


@permission_required('webapp.view_historiaClinica')
def detalle_historiaClinica(request, id):
    historiaClinicaVar = get_object_or_404(historiaClinica, id=id)
    #pacienteVar = paciente.objects.filter(historiaClinica=historiaClinica).order_by('fecha')
    data = {
        'historiaClinica': historiaClinicaVar,
        #'paciente': pacienteVar
    }
    return render(request, 'webapp/historiaClinica/detalle.html', data)


@permission_required('webapp.change_historiaClinica')
def modificar_historiaClinica(request, id):
    historiaClinicaVar = get_object_or_404(historiaClinica, id=id)
    data = {
        'form': historiaClinicaForm(instance=historiaClinicaVar)
    }
    if request.method == 'POST':
        formulario = historiaClinicaForm(
            data=request.POST, instance=historiaClinicaVar)
        if formulario.is_valid():
            formulario.save()
            messages.success(
                request, "historiaClinica modificada correctamente")
            return redirect(to="webapp:listar_historiaClinicas")
        else:
            data["form"] = formulario

    return render(request, 'webapp/historiaClinica/modificar.html', data)


@permission_required('webapp.delete_historiaClinica')
def eliminar_historiaClinica(request, id):
    historiaClinicaVar = get_object_or_404(historiaClinica, pk=id)
    historiaClinicaVar.delete()
    messages.success(request, "historiaClinica eliminada correctamente")
    return redirect(to="webapp:listar_historiaClinicas")

# ------------evoluciones-----------------------------------


@permission_required('webapp.add_evolucion')
def agregar_evolucion(request):
    data = {
        'form': evolucionForm()
    }
    if request.method == 'POST':
        formulario = evolucionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "evolucion agregado correctamente")
            return redirect(to="listar_evoluciones")
        else:
            data["form"] = formulario
    return render(request, 'webapp/evolucion/agregar.html', data)


@permission_required('webapp.view_evolucion')
def listar_evoluciones(request):
    evoluciones = evolucion.objects.all().order_by('fecha')
    data = {
        'evoluciones': evoluciones
    }
    return render(request, 'webapp/evolucion/listar.html', data)


@permission_required('webapp.view_evolucion')
def detalle_evolucion(request, id):
    evolucionVar = evolucion.objects.get(id=id)
    data = {
        'evolucion': evolucionVar
    }
    return render(request, 'webapp/evolucion/detalle.html', data)


@permission_required('webapp.change_evolucion')
def modificar_evolucion(request, id):
    evolucion = get_object_or_404(evolucion, pk=id)
    data = {
        'form': evolucionForm(instance=evolucion)
    }
    if request.method == 'POST':
        formulario = evolucionForm(data=request.POST, instance=evolucion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "evolucion modificado correctamente")
            return redirect(to="listar_evoluciones")
        else:
            data["form"] = formulario
    return render(request, 'webapp/evolucion/modificar.html', data)


@permission_required('webapp.delete_evolucion')
def eliminar_evolucion(request, id):
    evolucion = get_object_or_404(evolucion, id=id)
    evolucion.delete()
    messages.success(request, "evolucion eliminado correctamente")
    return redirect(to="listar_evoluciones")

    # ------------------------derivaciones-----------------------------------


@permission_required('webapp.add_derivacion')
def agregar_derivacion(request):
    derivacion = []
    data = {
        'form': derivacionForm()
    }
    if request.method == 'POST':
        formulario = derivacionForm(data=request.POST)
        if formulario.is_valid():
            derivacion = formulario.save(commit=False)
            derivacion.autor = User.objects.get(pk=request.user.id)
            derivacion.fecha = timezone.now()
            derivacion.status = 'activo'
            derivacion.save()
            messages.success(request, "derivacion agregado correctamente")
            return redirect(to="listar_derivaciones")
        else:
            data["form"] = formulario
    return render(request, 'webapp/derivacion/agregar.html', data)


@permission_required('webapp.view_derivacion')
def listar_derivaciones(request):
    derivaciones = derivacion.objects.all().order_by('fecha')
    data = {
        'derivaciones': derivaciones
    }
    return render(request, 'webapp/derivacion/listar.html', data)


@ permission_required('webapp.view_derivacion')
def detalle_derivacion(request, id):
    derivacionVar = get_object_or_404(derivacion, id=id)
    data = {
        'derivacion': derivacionVar,
    }
    return render(request, 'webapp/derivacion/detalle.html', data)


@ permission_required('webapp.change_derivacion')
def modificar_derivacion(request, id):
    derivacionVar = get_object_or_404(derivacion, id=id)
    data = {
        'form': derivacionForm(instance=derivacionVar)
    }
    if request.method == 'POST':
        formulario = derivacionForm(data=request.POST, instance=derivacionVar)
        if formulario.is_valid(commit=False):
            formulario.save()
            messages.success(request, "derivacion modificada correctamente")
            return redirect(to="listar_derivaciones")
        else:
            data["form"] = formulario

    return render(request, 'webapp/derivacion/modificar.html', data)


@ permission_required('webapp.delete_derivacion')
def eliminar_derivacion(request, id):
    derivacionVar = get_object_or_404(derivacion, id=id)
    derivacionVar.delete()
    messages.success(request, "derivacion eliminada correctamente")
    return redirect(to="listar_derivaciones")

