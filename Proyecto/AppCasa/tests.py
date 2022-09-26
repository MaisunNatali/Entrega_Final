import random
import string
from django.test import TestCase
from AppCasa.models import Hechizos, Post, Creadores

class HechizosTestCase(TestCase):

    def test_creacion_hechizos(self):
        # Test 1: Comprobar puedo crear un hechizo con un nombre  y descripción de letras random
        lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(128)]
        lista_letras_descripcion = [random.choice(string.ascii_letters + string.digits) for _ in range(150)]
        nombre_prueba = "".join(lista_letras_nombre)
        descripcion_prueba = "".join(lista_letras_descripcion)
        hechizo_1 = Hechizos.objects.create(nombre=nombre_prueba, descripcion=descripcion_prueba)

        self.assertIsNotNone(hechizo_1.id)

class PostTestCase(TestCase):

    def test_creacion_post(self):
        # Test 1: Comprobar puedo crear un post sin imagen
        title="Titulo prueba"
        subtitle="Subtitulo de prueba"
        content="Contenido de prueba"
        slug="prueba-1"
        author="Autor de prueba"

        post_1 = Post.objects.create(title=title,subtitle=subtitle,content=content, slug=slug,author=author)
            
        self.assertIsNotNone(post_1.id)

class CreadoresTestCase(TestCase):

    def test_creacion_creadores(self):
        # Test 1: Comprobar puedo crear un post sin imagen
        name="Nombre Prueba"
        lastname="Apellido Prueba"
        descripcion="Descripcion prueba"

        creador_1 = Creadores.objects.create(name=name,lastname=lastname, descripcion=descripcion)
            
        self.assertIsNotNone(creador_1.id)