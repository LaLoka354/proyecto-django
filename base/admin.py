from django.contrib import admin

# Register your models here.

from .models import Post, fichaTecnicaUsuario, Comment, CommentConsulta, NOVEDADES


admin.site.register(fichaTecnicaUsuario)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CommentConsulta)
admin.site.register(NOVEDADES)