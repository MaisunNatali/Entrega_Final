from typing import Dict

from django.shortcuts import render,redirect
from django.http import HttpResponse
from AppCasa.models import Casas, Estudiantes,Profesores, Hechizos ,Post,Inicio
from AppCasa.forms import CasasFormulario, EstudiantesFormulario, ProfesoresFormulario, UserRegisterForm,UserUpdateForm #, PostForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,TemplateView,DetailView
from django.contrib.auth.models import User

#Para el login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(request):
    picture=Inicio.objects.get(id=1)
    return render(request, "AppCasa/inicio.html",{'picture': picture})

#Casas

def casas(request):
    casas = Casas.objects.all()
    return render(request, "AppCasa/casas.html",{'casas': casas})

def casas_formulario(request):
    if request.method == 'POST':
            formulario= CasasFormulario(request.POST)

            if formulario.is_valid():
                data = formulario.cleaned_data
                casa = Casas(nombre=data['nombre'], fantasma=data['fantasma'])
                casa.save()
                return render(request, "AppCasa/inicio.html", {"exitoso": True})
    else:  # GET
            formulario= CasasFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCasa/form_casas.html", {"formulario": formulario})

def busqueda_casas(request):
    return render(request, "AppCasa/form_busqueda_casas.html")


def buscar(request):
    if request.GET["nombre"]:
            nombre = request.GET["nombre"]
            casas = Casas.objects.filter(nombre__icontains=nombre)
            return render(request, "AppCasa/casas.html", {'casas': casas})
    else:
            return render(request, "AppCasa/casas.html", {'cursos': []})

#Profesores
def profesores(request):
    profesores = Profesores.objects.all()
    contexto={'profesores':profesores}
    borrado=request.GET.get('borrado',None)
    contexto['borrado']=borrado
    actualizado=request.GET.get('actualizado',None)
    contexto['actualizado']=actualizado   
    return render(request, "AppCasa/profesores.html",contexto)

def profesores_formulario(request):
    if request.method == 'POST':
            formulario= ProfesoresFormulario(request.POST)

            if formulario.is_valid():
                data = formulario.cleaned_data
                profesor = Profesores(nombre=data['nombre'], apellido=data['apellido'],materia=data['materia'],casa=data['casa'])
                profesor.save()
                return render(request, "AppCasa/inicio.html",{"exitoso": True})
    else:  # GET
            formulario= ProfesoresFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCasa/form_profesores.html", {"formulario": formulario})

def eliminar_profesor(request,id):
    profesor= Profesores.objects.get(id=id)
    borrado_id=profesor.id
    profesor.delete()
    url_final=f"{reverse('profesores')}?borrado={borrado_id}"
    return redirect(url_final)

def actualizar_profesor(request,id):

    profesor=Profesores.objects.get(id=id)
    actualizado_id=profesor.id
    
    if request.method == 'POST':
            formulario= ProfesoresFormulario(request.POST)

            if formulario.is_valid():
                data = formulario.cleaned_data
                profesor.nombre=data['nombre']
                profesor.apellido=data['apellido']
                profesor.materia=data['materia']
                profesor.casa=data['casa']
                profesor.save()
            url_final=f"{reverse('profesores')}?actualizado={actualizado_id}"    
            return redirect(url_final)
    else:  # GET
            inicial={
                'nombre':profesor.nombre,
                'apellido':profesor.apellido,
                'materia':profesor.materia,
                'casa':profesor.casa
            }

            formulario= ProfesoresFormulario(initial=inicial)  
    return render(request, "AppCasa/form_profesores.html", {"formulario": formulario})

#Estudiantes
def estudiantes(request):
    estudiantes = Estudiantes.objects.all()  
    return render(request, "AppCasa/estudiantes.html",{'estudiantes':estudiantes})

def estudiantes_formulario(request):
    if request.method == 'POST':
            formulario= EstudiantesFormulario(request.POST)

            if formulario.is_valid():
                data = formulario.cleaned_data
                estudiante = Estudiantes(nombre=data['nombre'], apellido=data['apellido'],casa=data['casa'])
                estudiante.save()
                return render(request, "AppCasa/inicio.html",{"exitoso": True})
    else:  # GET
            formulario= EstudiantesFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCasa/form_estudiantes.html",{"formulario": formulario})


#Hechizos

class HechizosListView(ListView):
    model=Hechizos
    template_name='AppCasa/hechizos.html'

class HechizosCreateView(CreateView):
    model=Hechizos
    fields=['nombre','descripcion']
    success_url=reverse_lazy('hechizos')

class HechizosUpdateView(UpdateView):
    model = Hechizos
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('hechizos')

class HechizosDeleteView(DeleteView):
    model = Hechizos
    success_url = reverse_lazy('hechizos')

#Registro

def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "AppCasa/inicio.html", {"mensaje": "El registro fue realizado con éxito"})
        else:
            mensaje = 'Error detectado en el registro'
    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "AppCasa/registro.html", context=context)

#Login y Logout

def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return render(request, "AppCasa/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"AppCasa/inicio.html", {"mensaje":"Error, vuelva a intentarlo"})
        else:
            return render(request,"AppCasa/inicio.html", {"mensaje":"Error, vuelva a intentarlo"})

    form = AuthenticationForm()
    return render(request,"AppCasa/login.html", {'form':form} )


class CustomLogoutView(LogoutView):
    template_name = 'AppCasa/logout.html'
    next_page = reverse_lazy('logout')

# Editar datos de usuario
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'AppCasa/form_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

# Entradas de blog

class PostListView(ListView):
    model=Post
    template_name='AppCasa/post.html'


    
#Mostrar un blog especifico
class PostDetailView(DetailView):
    model = Post
    template_name = 'AppCasa/post_detail.html'



#Crear, actualizar y eliminar un blog

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'subtitle', 'content', 'slug','author']
    success_url = reverse_lazy('inicio')


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'content', 'slug','author']
    success_url = reverse_lazy('inicio')


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('inicio')

