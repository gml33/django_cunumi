from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, pacienteForm, pacienteForm, historiaClinicaForm, evolucionForm, derivacionForm, facturaForm, pagoForm, turnoForm, informeForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .bot import bot, chat_id
from .models import paciente,historiaClinica, evolucion, derivacion, factura, pago ,turno, informe
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def home(request):
    return render(request, 'registro/index.html')

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
    pacientes_all = paciente.objects.all()
    paginator = Paginator(pacientes_all, 20)
    page = request.GET.get('page')
    pacientes = paginator.get_page(page)
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
    return render(request, 'webapp/paciente/agregar.html', context=context)

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
@login_required(login_url='my-login')
def agregar_historiaClinica(request):
    data = {
        'form': historiaClinicaForm()
    }
    if request.method == 'POST':
        formulario = historiaClinicaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "historiaClinica agregada correctamente")
            return redirect(to="listar_historiasClinicas")
        else:
            data["form"] = formulario
    return render(request, 'webapp/historiaClinica/agregar.html', data)


@login_required(login_url='my-login')
def listar_historiasClinicas(request):
    historiasClinicas = historiaClinica.objects.all().order_by('fecha')
    data = {
        'historiasClinicas': historiasClinicas
    }
    return render(request, 'webapp/historiaClinica/listar.html', data)


@login_required(login_url='my-login')
def detalle_historiaClinica(request, id):
    historiaClinicaVar = get_object_or_404(historiaClinica, id=id)
    #pacienteVar = paciente.objects.filter(historiaClinica=historiaClinica).order_by('fecha')
    data = {
        'historiaClinica': historiaClinicaVar,
        #'paciente': pacienteVar
    }
    return render(request, 'webapp/historiaClinica/detalle.html', data)


@login_required(login_url='my-login')
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
            return redirect(to="listar_historiasClinicas")
        else:
            data["form"] = formulario

    return render(request, 'webapp/historiaClinica/modificar.html', data)


@login_required(login_url='my-login')
def eliminar_historiaClinica(request, id):
    historiaClinicaVar = get_object_or_404(historiaClinica, pk=id)
    historiaClinicaVar.delete()
    messages.success(request, "historiaClinica eliminada correctamente")
    return redirect(to="listar_historiasClinicas")

# ------------evoluciones-----------------------------------


@login_required(login_url='my-login')
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


@login_required(login_url='my-login')
def listar_evoluciones(request):
    evoluciones = evolucion.objects.all().order_by('fecha')
    data = {
        'evoluciones': evoluciones
    }
    return render(request, 'webapp/evolucion/listar.html', data)


@login_required(login_url='my-login')
def detalle_evolucion(request, id):
    evolucionVar = evolucion.objects.get(id=id)
    data = {
        'evolucion': evolucionVar
    }
    return render(request, 'webapp/evolucion/detalle.html', data)


@login_required(login_url='my-login')
def modificar_evolucion(request, id):
    evolucion_seleccionada = get_object_or_404(evolucion, pk=id)
    data = {
        'form': evolucionForm(instance=evolucion_seleccionada)
    }
    if request.method == 'POST':
        formulario = evolucionForm(data=request.POST, instance=evolucion_seleccionada)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "evolucion modificado correctamente")
            return redirect(to="listar_evoluciones")
        else:
            data["form"] = formulario
    return render(request, 'webapp/evolucion/modificar.html', data)


@login_required(login_url='my-login')
def eliminar_evolucion(request, id):
    evolucion_seleccionada = get_object_or_404(evolucion, id=id)
    evolucion_seleccionada.delete()
    messages.success(request, "evolucion eliminada correctamente")
    return redirect(to="listar_evoluciones")

    # ------------------------derivaciones-----------------------------------


@login_required(login_url='my-login')
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


@login_required(login_url='my-login')
def listar_derivaciones(request):
    derivaciones = derivacion.objects.all().order_by('fecha')
    data = {
        'derivaciones': derivaciones
    }
    return render(request, 'webapp/derivacion/listar.html', data)


@login_required(login_url='my-login')
def detalle_derivacion(request, id):
    derivacionVar = get_object_or_404(derivacion, id=id)
    data = {
        'derivacion': derivacionVar,
    }
    return render(request, 'webapp/derivacion/detalle.html', data)


@login_required(login_url='my-login')
def modificar_derivacion(request, id):
    derivacionVar = get_object_or_404(derivacion, id=id)
    data = {
        'form': derivacionForm(instance=derivacionVar)
    }
    if request.method == 'POST':
        formulario = derivacionForm(data=request.POST, instance=derivacionVar)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "derivacion modificada correctamente")
            return redirect(to="listar_derivaciones")
        else:
            data["form"] = formulario

    return render(request, 'webapp/derivacion/modificar.html', data)


@login_required(login_url='my-login')
def eliminar_derivacion(request, id):
    derivacionVar = get_object_or_404(derivacion, id=id)
    derivacionVar.delete()
    messages.success(request, "derivacion eliminada correctamente")
    return redirect(to="listar_derivaciones")

# ---------------------------facturas--------------------------------
@login_required(login_url='my-login')
def agregar_factura(request):
    data = {
        'form': facturaForm()
    }
    if request.method == 'POST':
        formulario = facturaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Factura agregada correctamente")
            return redirect(to="listar_facturas")
        else:
            data["form"] = formulario
    return render(request, 'webapp/factura/agregar.html', data)


@login_required(login_url='my-login')
def listar_facturas(request):
    facturas = factura.objects.all().order_by('fecha')
    data = {
        'facturas': facturas
    }
    return render(request, 'webapp/factura/listar.html', data)


@login_required(login_url='my-login')
def detalle_factura(request, id):
    facturaVar = get_object_or_404(factura, id=id)
    data = {
        'factura': facturaVar,
    }
    return render(request, 'webapp/factura/detalle.html', data)


@login_required(login_url='my-login')
def modificar_factura(request, id):
    facturaVar = get_object_or_404(factura, id=id)
    data = {
        'form': facturaForm(instance=facturaVar)
    }
    if request.method == 'POST':
        formulario = facturaForm(
            data=request.POST, instance=facturaVar)
        if formulario.is_valid():
            formulario.save()
            messages.success(
                request, "Factura modificada correctamente")
            return redirect(to="listar_facturas")
        else:
            data["form"] = formulario

    return render(request, 'webapp/factura/modificar.html', data)


@login_required(login_url='my-login')
def eliminar_factura(request, id):
    facturaVar = get_object_or_404(factura, pk=id)
    facturaVar.delete()
    messages.success(request, "Factura eliminada correctamente")
    return redirect(to="listar_facturas")


# ---------------------------turnos--------------------------------
@login_required(login_url='my-login')
def agregar_turno(request):
    data = {
        'form': turnoForm()
    }
    if request.method == 'POST':
        formulario = turnoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "turno agregado correctamente")
            return redirect(to="listar_turnos")
        else:
            data["form"] = formulario
    return render(request, 'webapp/turno/agregar.html', data)


@login_required(login_url='my-login')
def listar_turnos(request):
    turnos = turno.objects.all().order_by('fecha')
    data = {
        'turnos': turnos
    }
    return render(request, 'webapp/turno/listar.html', data)


@login_required(login_url='my-login')
def detalle_turno(request, id):
    turnoVar = get_object_or_404(turno, id=id)
    data = {
        'turno': turnoVar,
    }
    return render(request, 'webapp/turno/detalle.html', data)


@login_required(login_url='my-login')
def modificar_turno(request, id):
    turnoVar = get_object_or_404(turno, id=id)
    data = {
        'form': turnoForm(instance=turnoVar)
    }
    if request.method == 'POST':
        formulario = turnoForm(
            data=request.POST, instance=turnoVar)
        if formulario.is_valid():
            formulario.save()
            messages.success(
                request, "Turno modificado correctamente")
            return redirect(to="listar_turnos")
        else:
            data["form"] = formulario

    return render(request, 'webapp/turno/modificar.html', data)


@login_required(login_url='my-login')
def eliminar_turno(request, id):
    turnoVar = get_object_or_404(turno, pk=id)
    turnoVar.delete()
    messages.success(request, "Turno eliminado correctamente")
    return redirect(to="listar_turnos")