from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('login/', views.loginPage),
    path('logout/', views.logoutPage),
    path('register/', views.registerPage),
    path('post/', views.post),
    path('consulta/', views.ficha),
    path('ficha/<int:id>', views.viewFicha),
    path('home_fichas/', views.homeFichas),
    path('comment/', views.comment),
    path('consulta_comment/', views.comentarios),
    path('consulta_comment_make/', views.commentConsulta),
    path('post/<int:id>', views.viewCompleta, name='view_notice'),
    path('comment/<int:id>/', views.comment, name='comment'),
    path('novedades_make/', views.Novedades)

]

