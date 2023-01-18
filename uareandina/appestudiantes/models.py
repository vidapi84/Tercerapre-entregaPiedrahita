from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    curso = models.IntegerField()
    fecha_inicio = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.curso}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"



