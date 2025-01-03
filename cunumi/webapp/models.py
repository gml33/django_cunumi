from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    rol_choices = (
        ('administrativo', 'administrativo'),
        ('Psicologo', 'Psicologo'),
        ('Fonoaudiologo', 'Fonoaudiologo'),
        ('psiquiatra', 'psiquiatra'),
        ('psicopedagogo','psicopedagogo'),
        ('otro','otro'))
    rol = models.CharField(max_length=25, choices=rol_choices, default='Psicologo')
    comentario = models.TextField(blank=True)

    def __str__(self):
        return self.username


class paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    dni = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    edad = models.IntegerField(blank=True)
    localidad = models.CharField(max_length=100, blank=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    responables = models.CharField(max_length=200, blank=True)
    motivo_consulta = models.CharField(max_length=200, blank=True)
    derivado = models.BooleanField(default=False)
    email = models.EmailField(blank=True)
    estado_choices = (
        ('activo', 'activo'),
        ('inactivo', 'inactivo'),
        ('alta', 'alta'),
        ('derivado', 'derivado'))
    estado = models.CharField(max_length=20, choices=estado_choices, default='activo')
    profesional_responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class historiaClinica(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=False)
    fecha = models.DateField(blank=True)
    detalle = models.TextField(blank=True)
    profesional_responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"


class evolucion(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=False)
    fecha = models.DateField(blank=True, null=True)
    detalle = models.TextField(blank=True)
    profesional_responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"


class derivacion(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=False)
    fecha = models.DateField(blank=True, null=True)
    motivo = models.TextField(blank=True)
    detalle = models.TextField(blank=True)
    profesional_responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False)

class factura(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE, blank=True)
    mes_choices = (
        ('Enero','Enero'),
        ('Febrero','Febrero'),
        ('Marzo','Marzo'),
        ('Abril','Abril'),
        ('Mayo','Mayo'),
        ('Junio','Junio'),
        ('Julio','Julio'),
        ('Agosto','Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre','Octubre'),
        ('Noviembre','Noviembre'),
        ('Diciembre','Diciembre')
    )
    mes = models.CharField(max_length=20, choices=mes_choices, default='Enero')
    fecha = models.DateField(blank=True, null=True)
    monto = models.IntegerField(blank=True)
    identificador = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.numero} - {self.fecha}"


class pago(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE, blank=False)
    fecha = models.DateField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    motivo_choices = (('consulta','consulta'),
                      ('informe','informe'),
                      ('psicotecnico','psicotecnico'),
                      ('peritaje','peritaje'),
                      ('apto','apto'))
    motivo= models.CharField(max_length=20, choices=motivo_choices, default='consulta')
    estado_choices = (
        ('pendiente', 'pendiente'),
        ('saldado', 'saldado'))
    estado = models.CharField(max_length=20, choices=estado_choices, default='pendiente')
    factura = models.ForeignKey(factura, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha} - ${self.monto}"

class turno(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE, blank=False)
    fecha = models.DateField(blank=True, null=True)
    hora_choices = (
        ('8:00-8:45','8:00-8:45'),
        ('8:45-9:30','8:45-9:30'),
        ('9:30-10:15','9:30-10:15'),
        ('10:15-11:00','10:15-11:00'),
        ('11:00-11:45','11:00-11:45'),
        ('11:45-12:30','11:45-12:30'),
        ('12:30-13:15','12:30-13:15'),
        ('13:15-14:00','13:15-14:00'),
        ('14:00-14:45','14:00-14:45'),
        ('14:45-15:30','14:45-15:30'),
        ('15:30-16:15','15:30-16:15'),
        ('16:15-17:00','16:15-17:00'),
        ('17:00-17:15','17:00-17:15'),
        ('17:15-18:30','17:15-18:30'),
        ('18:30-19:15','18:30-19:15'),
        ('19:15-20:00','19:15-20:00'),
        ('20:00-20:45','20:00-20:45'),
        ('20:45-21:30','20:45-21:30')
    )
    hora = models.CharField(max_length=20, choices=hora_choices, default='1')
    disponible = models.BooleanField(blank=True, default=False)
    asistio = models.BooleanField(default=False)
    profesional_responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"

class informe(models.Model):
    paciente = models.ForeignKey(
        paciente, on_delete=models.CASCADE, blank=True)
    fecha = models.DateField(blank=True, null=True)
    detalle = models.TextField(blank=True)
    profesional_responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"
    
