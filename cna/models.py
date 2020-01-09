from django.db import models

class Escuela(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre


class Programa(models.Model):
    nombre = models.CharField(max_length=150)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class FactorCna(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


class Caracteristica(models.Model):
    factor = models.ForeignKey(FactorCna, on_delete= models.CASCADE)
    descripcion = models.TextField(max_length=250)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion


class MetaLP(models.Model):
    descripcion = models.TextField(max_length=300)
    caracteristica = models.ForeignKey(Caracteristica, on_delete= models.CASCADE)

    def __str__(self):
        return self.descripcion


class MetaCP(models.Model):
    descripcion = models.TextField(max_length=300)
    caracteristica = models.ForeignKey(Caracteristica, on_delete= models.CASCADE)

    def __str__(self):
        return self.descripcion

class Objetivo(models.Model):
    descripcion = models.TextField(max_length=500)
    caracteristica = models.ForeignKey(Caracteristica, on_delete= models.CASCADE)

    def __str__(self):
        return self.descripcion








