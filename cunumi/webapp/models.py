#paciente
#historia clinica
#pago
#derivacion
#evolucion
#turno
#informe

#profesional-colega


from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    dni = models.CharField(max_length=100, blank=True)
    edad = models.IntegerField(blank=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    responables = models.CharField(max_length=200, blank=True)
    motivo_consulta = models.CharField(max_length=200, blank=True)
    derivado = models.BooleanField(default=False)
    telefono = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    estado_choices = (
        ('activo', 'activo'),
        ('inactivo', 'inactivo'),
        ('alta', 'alta'),
        ('derivado', 'derivado')
    )
    estado = models.CharField(max_length=20, choices=estado_choices, default='activo')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class historiaClinica(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=True)
    fecha = models.DateField(blank=True, null=True)
    detalle = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"


class evolucion(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=True)
    fecha = models.DateField(blank=True, null=True)
    detalle = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"


class derivacion(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=True)
    fecha = models.DateField(blank=True, null=True)
    motivo = models.TextField(blank=True)
    detalle = models.TextField(blank=True)
    profesional = models.CharField(max_length=200, blank=True)


class pago(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE, blank=False)
    fecha = models.DateField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    motivo_choices = (('consulta','consulta'),
                      ('informe','informe'),
                      ('psicotecnico','psicotecnico'),
                      ('peritaje','peritaje'),
                      ('apto','apto')
                      )
    motivo= models.CharField(max_length=20, choices=motivo_choices, default='consulta')
    estado_choices = (
        ('pendiente', 'pendiente'),
        ('saldado', 'saldado')
    )
    estado = models.CharField(max_length=20, choices=estado_choices, default='pendiente')

class turno(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE, blank=False)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    asistio = models.BooleanField(default=False)

class informe(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=True)
    fecha = models.DateField(blank=True, null=True)
    detalle = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"
