from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

#Blog
class Post(models.Model):
        
    title=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    content=models.TextField()
    slug=models.SlugField(max_length=250,null=False, unique=True)
    published=models.DateTimeField(default=timezone.now)
    author=models.CharField(max_length=60)
    imagen = models.ImageField(upload_to='post', null=True, blank = True)

    def __str__(self) -> str:
        return f' {self.title} de {self.author}'

# Para colocar imagen en el inicio
class Inicio(models.Model):
    
    imagen = models.ImageField(upload_to='inicio', null=True, blank = True)
    def __str__(self):
        return f"Imagen de inicio"

class Creadores(models.Model):
        
    name=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    descripcion=models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='creador', null=True, blank = True)

    def __str__(self) -> str:
        return f' {self.name} {self.lastname}'