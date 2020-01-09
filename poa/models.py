from django.db import models

from cna.models import Objetivo

class EstadoActividad(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Dependencia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#class MedioVerificacion(models.Model):
#    descripcion = models.TextField(max_length=250)

class Responsable(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cargo = models.CharField(max_length=55)
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    #usuario ==> por aca iria la relacion con el modelo User

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)

class Actividad(models.Model):
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=250)
    frecuencia = models.PositiveIntegerField()
    descripcion_fecha = models.CharField(max_length=150)
    cant_actividades_cumplidas = models.PositiveIntegerField()
    cant_actividades_no_realizadas = models.PositiveIntegerField()
    estado = models.ForeignKey(EstadoActividad, on_delete = models.CASCADE)
    dependencias = models.ManyToManyField(Dependencia)
    medios_verificacion = models.CharField(max_length=200)
    

    def __str__(self):
        return self.descripcion



