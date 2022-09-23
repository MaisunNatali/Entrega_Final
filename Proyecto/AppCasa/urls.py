from django.urls import path

from AppCasa import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    #Casas
    path('casas/', views.casas, name="casas"),
    path('crear-casa/', views.casas_formulario, name="casas_formulario"),
    path('busqueda-casa-form/', views.busqueda_casas, name="busqueda_casas_form"),
    path('busqueda-casa/', views.buscar, name="busqueda_casas"), 
    #Estudiantes
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('agregar-estudiantes/', views.estudiantes_formulario, name="estudiantes_formulario"),
    #Profesores
    path('profesores/', views.profesores, name="profesores"),
    path('agregar-profesores/', views.profesores_formulario, name="profesores_formulario"),
    path('actualizar-profesores/<int:id>/', views.actualizar_profesor, name="actualizar_profesor"),
    path('eliminar_profesor/<int:id>/',views.eliminar_profesor,name="eliminar_profesor"),
    #Hechizos
    path('hechizos/', views.HechizosListView.as_view(), name="hechizos"),
    path('crear-hechizo/', views.HechizosCreateView.as_view(), name="crear_hechizo"),
    path('editar-hechizo/<int:pk>/', views.HechizosUpdateView.as_view(), name="editar_hechizo"),
    path('eliminar-hechizo/<int:pk>/', views.HechizosDeleteView.as_view(), name="eliminar_hechizo"),

    #Registro
    path('register/', views.register, name = 'register'),

    #Login y logout
    path('accounts/login//', views.login_request, name = 'login'),  
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),

    #Editar datos de perfil
    path('accounts/profile/', views.ProfileUpdateView.as_view(), name="editar_perfil"),

    #Blog
    path('post/', views.PostListView.as_view(), name="blog_home"),

    #Ver un post especifico
    path('<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),

    #Crear un post y actualizar
    path('crear-blog/', views.PostCreateView.as_view(), name="post_create"),
    path('editar-blog/<int:pk>/', views.PostUpdateView.as_view(), name="post_update"),

    #Eliminar post
    path('eliminar-blog/<int:pk>/', views.PostDeleteView.as_view(), name="post_delete"),

]