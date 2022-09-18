from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Casas(models.Model):
    nombre = models.CharField(max_length=128)
    fantasma = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.nombre}'

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    casa = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
    
class Profesores(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    materia=models.CharField(max_length=128)
    casa = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.nombre}, {self.apellido} Prof. de {self.materia}'

class Hechizos(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.nombre}'

class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcarpeta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"Imagen de: {self.user}"