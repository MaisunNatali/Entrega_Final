from django.contrib import admin
from AppCasa.models import Casas, Estudiantes,Profesores,Avatar,Category,Post
# Register your models here.
admin.site.register(Casas)
admin.site.register(Estudiantes)
admin.site.register(Profesores)
admin.site.register(Avatar)
admin.site.register(Category)

@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('title','id','status','slug','author')
    prepopulated_fields={'slug':('title',),}



