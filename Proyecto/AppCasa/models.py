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
class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
        
    options=(
        ('draft','Draft'),
        ('published','Published')
        )

    category=models.ForeignKey(Category, on_delete=models.PROTECT,default=1)
    title=models.CharField(max_length=255)
    excerpt=models.TextField(null=True)
    content=models.TextField()
    slug=models.SlugField(max_length=250, unique_for_date="published",null=False, unique=True)
    published=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    status=models.CharField(max_length=10,choices=options,default='draft')
    objects=models.Manager() #default manager
    postobjects=PostObjects() #custom manager
    
    class Meta:
        ordering=('-published',)
    
    def __str__(self) -> str:
        return self.title
