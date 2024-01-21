from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    short_description = models.CharField(max_length=600)
    text = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.title 

class fichaTecnicaUsuario(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=12)
    birthday = models.CharField(max_length=10, null=True)
    birth_place = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=100, null=True)
    motivo_consulta = models.TextField(null=True)
    marital_status = models.CharField(max_length=40, null=True)
    diagnosticos = models.TextField(null=True)
    pregunta_1 = models.TextField(null=True)
    pregunta_2 = models.TextField(null=True)
    pregunta_3 = models.TextField(null=True)
    forma_nacimiento = models.TextField(null=True)
    meses_gestacion = models.SmallIntegerField(null=True)
    conflictos_embarazo = models.TextField(null=True)
    otros_hechos_embarazo = models.TextField(null=True)
    n_hijo = models.SmallIntegerField(null=True)

class Comment(models.Model):
    text=models.TextField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

class CommentConsulta(models.Model):
    text=models.TextField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    
class NOVEDADES(models.Model):
    text=models.TextField(null=True)
    user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

