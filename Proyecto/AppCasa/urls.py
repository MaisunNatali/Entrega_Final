from django.urls import path

from AppCasa import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('casas/', views.casas, name="casas"),
    path('crear-casa/', views.casas_formulario, name="casas_formulario"),
    path('busqueda-casa-form/', views.busqueda_casas, name="busqueda_casas_form"),
    path('busqueda-casa/', views.buscar, name="busqueda_casas"), 
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('agregar-estudiantes/', views.estudiantes_formulario, name="estudiantes_formulario"),
    path('profesores/', views.profesores, name="profesores"),
    path('agregar-profesores/', views.profesores_formulario, name="profesores_formulario"),
    path('actualizar-profesores/<int:id>/', views.actualizar_profesor, name="actualizar_profesor"),
    path('eliminar_profesor/<int:id>/',views.eliminar_profesor,name="eliminar_profesor"),

]