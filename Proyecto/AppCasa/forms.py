from socket import fromshare
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCasa.models import Post

class CasasFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    fantasma = forms.CharField(max_length=128)


class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    casa=forms.CharField(max_length=128)


class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    materia=forms.CharField(max_length=128)
    casa=forms.CharField(max_length=128)


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']
        
# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Post

#         fields = ['title', 'subtitle', 'content', 'slug']