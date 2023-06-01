from django.contrib import admin
from .models import paciente, historiaClinica, evolucion,  derivacion, pago, turno, informe, factura


class pacienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "edad", 'dni', "estado", "profesional_responsable"]
    #list_editable = ["estado", "profesional_responsable" ]
    search_fields = ["nombre", 'apellido', 'estado', "profesional_responsable"]
    list_filter = ["estado", "profesional_responsable"]
    list_per_page = 50


class historiaClinicaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fecha', 'profesional_responsable']
    #list_editable = ['detalle']
    search_fields = ['fecha']
    list_per_page = 10


class evolucionAdmin(admin.ModelAdmin):
    list_display = ["fecha", "paciente", 'profesional_responsable']
    search_fields = ["fecha", "paciente"]
    list_filter = ["fecha", "paciente"]


class derivacionAdmin(admin.ModelAdmin):
    list_display = ["paciente", 'fecha']
    search_fields = ["paciente", "fecha"]
    list_filter = ['paciente', 'fecha']
    list_per_page = 50

class pagoAdmin(admin.ModelAdmin):
    list_display = ["paciente", 'fecha', 'monto', 'estado']
    search_fields = ["paciente", "fecha"]
    list_filter = ['paciente', 'fecha']
    list_per_page = 50

class turnoAdmin(admin.ModelAdmin):
    list_display = ["paciente", 'fecha', 'asistio']
    search_fields = ["paciente", "fecha"]
    list_filter = ['paciente', 'fecha']
    list_per_page = 50

class informeAdmin(admin.ModelAdmin):
    list_display = ["paciente", 'fecha', 'profesional_responsable']
    search_fields = ["paciente", "fecha"]
    list_filter = ['paciente', 'fecha']
    list_per_page = 50

class facturaAdmin(admin.ModelAdmin):
    list_display = ["paciente", 'fecha', 'monto', 'numero']
    search_fields = ["paciente", "fecha", 'monto', 'numero']
    list_filter = ['paciente', 'fecha']
    list_per_page = 50

    # Register your models here.
admin.site.register(paciente, pacienteAdmin)
admin.site.register(historiaClinica, historiaClinicaAdmin)
admin.site.register(evolucion, evolucionAdmin)
admin.site.register(derivacion, derivacionAdmin)
admin.site.register(pago, pagoAdmin)
admin.site.register(turno, turnoAdmin)
admin.site.register(informe, informeAdmin)
admin.site.register(factura, facturaAdmin)
