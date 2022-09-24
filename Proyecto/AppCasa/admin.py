from django.contrib import admin
from AppCasa.models import Casas, Estudiantes,Profesores,Avatar,Post,Inicio,Creadores
# Register your models here.
admin.site.register(Casas)
admin.site.register(Estudiantes)
admin.site.register(Profesores)
admin.site.register(Avatar)
admin.site.register(Inicio)
admin.site.register(Creadores)

@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('title','id','slug','author')

