from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import paciente, historiaClinica, evolucion,  derivacion, pago, turno, informe, factura, Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('rol','comentario')}),
    )

class pacienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "edad", 'dni', "estado", "profesional_responsable"]
    #list_editable = ["estado", "profesional_responsable" ]
    search_fields = ["nombre", 'apellido', 'estado', "profesional_responsable"]
    list_filter = ["estado", "profesional_responsable"]
    list_per_page = 50
    verbose_name_plural = 'Pacientes'


class historiaClinicaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fecha', 'profesional_responsable']
    #list_editable = ['detalle']
    search_fields = ['fecha']
    list_per_page = 10
    verbose_name_plural = 'Historias Clínicas'


class evolucionAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Evoluciones'
    list_display = ["fecha", "paciente", 'profesional_responsable']
    search_fields = ["fecha", "paciente"]
    list_filter = ["fecha", "paciente"]   


class derivacionAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Derivaciones'
    list_display = ["paciente", 'fecha']
    search_fields = ["paciente", "fecha"]
    list_filter = ['paciente', 'fecha']
    list_per_page = 50

class pagoAdmin(admin.ModelAdmin):
    list_display = ["paciente", 'fecha', 'monto', 'estado']
    search_fields = ["paciente", "fecha"]
    list_filter = ['paciente', 'fecha']
    list_per_page = 50
    verbose_name_plural = 'Pagos'

class turnoAdmin(admin.ModelAdmin):
    list_display = ["paciente", 'fecha', 'hora','disponible', 'asistio']
    search_fields = ["paciente", "fecha"]
    list_filter = ['paciente', 'fecha']
    list_per_page = 50
    verbose_name_plural = 'Turnos'

class informeAdmin(admin.ModelAdmin):
    list_display = ["paciente", 'fecha', 'profesional_responsable']
    search_fields = ["paciente", "fecha"]
    list_filter = ['paciente', 'fecha']
    list_per_page = 50
    verbose_name_plural = 'Informes'

class facturaAdmin(admin.ModelAdmin):
    list_display = ["paciente", 'fecha', 'monto', 'identificador']
    search_fields = ["paciente", "fecha", 'monto', 'identificador']
    list_filter = ['paciente', 'fecha']
    list_per_page = 50
    verbose_name_plural = 'Facturas'

    # Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(paciente, pacienteAdmin)
admin.site.register(historiaClinica, historiaClinicaAdmin)
admin.site.register(evolucion, evolucionAdmin)
admin.site.register(derivacion, derivacionAdmin)
admin.site.register(pago, pagoAdmin)
admin.site.register(turno, turnoAdmin)
admin.site.register(informe, informeAdmin)
admin.site.register(factura, facturaAdmin)
