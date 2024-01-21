from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post, fichaTecnicaUsuario, Comment, CommentConsulta, NOVEDADES
from django.http import HttpResponseRedirect


def loginPage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username = username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "se ha iniciado sesion correctamente.")
                return redirect('/')
            messages.error(request, "usuario o contraseña incorrectos")
    return render(request, 'login.html')

def registerPage(request):
    if request.method =='POST':
         username = request.POST.get('username')
         first_name = request.POST.get('first_name')
         last_name = request.POST.get('last_name')
         email = request.POST.get('email')
         password = request.POST.get('password')
         confirm_password = request.POST.get('confirm_password')
         if (password != confirm_password):
            messages.error(request, 'las contraseñas no coinciden')
            return redirect('/')
         User.objects.create_user(username, first_name=first_name, last_name=last_name, email=email, password=password)
         messages.success(request, "usted se ha registrado correctamente")
         return redirect('/login')
    return render(request, 'register.html')

def home(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by('-created')[:5]
    
    total_novedades = NOVEDADES.objects.count()
    novedades = NOVEDADES.objects.order_by('-created')[:1]
    
    return render(request, 'home.html', {'novedades': novedades, 'total_novedades': total_novedades, 'posts': posts, 'total_posts': total_posts})


def homeFichas(request):
    fichas = fichaTecnicaUsuario.objects.all()
    return render(request, 'home_fichas.html', {'fichas': fichas})

def viewCompleta(request, id = None):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        id = request.POST.get('id')
        p = Post.objects.get(id = id)
        p.title = request.POST.get('title')
        p.text = request.POST.get('text')
        p.short_description = request.POST.get('short_description')
        p.save()
    context = {}
    if id is not None:
                p = Post.objects.get(id = id)
                context['post'] = p
    return render(request, 'view_notice.html', {'post': post})

def viewFicha(request, id = None):
        if request.method == 'POST':
            id = request.POST.get('id')
            p = fichaTecnicaUsuario.objects.get(id = id)
            p.first_name = request.POST.get('first_name')
            p.last_name = request.POST.get('last_name')
            p.phone_number = request.POST.get('phone_number')
            p.birthday = request.POST.get('birthday')
            p.birth_place = request.POST.get('birth_place')
            p.email = request.POST.get('email')
            p.motivo_consulta = request.POST.get('motivo_consulta')
            p.marital_status = request.POST.get('marital_status')
            p.diagnosticos = request.POST.get('diagnosticos')
            p.pregunta_1 = request.POST.get('pregunta1')
            p.pregunta_2 = request.POST.get('pregunta2')
            p.pregunta_3 = request.POST.get('pregunta3')
            p.forma_nacimiento = request.POST.get('forma_nacimiento')
            p.meses_gestacion = request.POST.get('meses_gestacion')
            p.conflictos_embarazo = request.POST.get('conflictos_embarazo')
            p.otros_hechos_embarazo = request.POST.get('otros_hechos_embarazo')
            p.n_hijo = request.POST.get('n_hijo')
        context = {}
        if id is not None:
                p = fichaTecnicaUsuario.objects.get(id = id)
                context['ficha'] = p
        return render(request, 'view_ficha.html', context)

def post(request, id=None):
    if request.method == 'POST':
        form_id = request.POST.get('id')
        title = request.POST.get('title')
        text = request.POST.get('text')
        short_description = request.POST.get('short_description')
        user = request.user

        if not form_id:
            # Si no hay un ID en el formulario, es una nueva publicación
            Post.objects.create(
                title=title,
                text=text,
                short_description=short_description,
                user = user
            )
            messages.success(request, "el post se creó nashemente")
            return redirect('/home')
        else:
            # Si hay un ID en el formulario, es una edición
            post = get_object_or_404(Post, id=form_id)
            post.title = title
            post.text = text
            post.short_description = short_description
            post.save()

        # Redirigir a la página de detalle de la publicación recién creada o editada
        return HttpResponseRedirect('/')

    context = {}
    if id is not None:
        post = get_object_or_404(Post, id=id)
        context['post'] = post

    return render(request, 'ejemplo.html', context)

def ficha(request):
    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        birthday = request.POST.get('birthday')
        birth_place = request.POST.get('birth_place')
        email = request.POST.get('email')
        motivo_consulta = request.POST.get('motivo_consulta')
        marital_status = request.POST.get('marital_status')
        diagnosticos = request.POST.get('diagnosticos')
        pregunta_1 = request.POST.get('pregunta1')
        pregunta_2 = request.POST.get('pregunta2')
        pregunta_3 = request.POST.get('pregunta3')
        forma_nacimiento = request.POST.get('forma_nacimiento')
        meses_gestacion = request.POST.get('meses_gestacion')
        conflictos_embarazo = request.POST.get('conflictos_embarazo')
        otros_hechos_embarazo = request.POST.get('otros_hechos_embarazo')
        n_hijo = request.POST.get('n_hijo')
        fichaTecnicaUsuario.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number, birthday=birthday, birth_place=birth_place, email=email, motivo_consulta=motivo_consulta, marital_status=marital_status, diagnosticos=diagnosticos, pregunta_1=pregunta_1, pregunta_2=pregunta_2, pregunta_3=pregunta_3, forma_nacimiento=forma_nacimiento, meses_gestacion=meses_gestacion, conflictos_embarazo=conflictos_embarazo, otros_hechos_embarazo=otros_hechos_embarazo, n_hijo=n_hijo)
        messages.success(request, "su ficha se ha enviado correctamente, lo contactaremos a la brevedad")
        return redirect('/')
    return render(request, 'agendarConsulta.html')

def comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post')
        post = get_object_or_404(Post, pk=post_id)
        
        Comment.objects.create(
            text=request.POST.get('text'),
            user=request.user,
            post=post
        )
        messages.success(request, "publicacion exitosa")
        return redirect('/')
    return render(request, 'view_notice.html')

def logoutPage(request):
    logout(request)
    messages.success(request, "se ha cerrado sesión correctamente")
    return redirect('/')

def comentarios(request):
    total_comments = CommentConsulta.objects.count()
    comments = CommentConsulta.objects.order_by('-created')
    return render(request, 'comentarios.html', {'comments': comments, 'total_comments': total_comments})

def commentConsulta(request):
    if request.method == 'POST':
        CommentConsulta.objects.create(
            text=request.POST.get('text'),
            user=request.user,
        )
        messages.success(request, "publicacion exitosa")
        return redirect('/consulta_comment')
    return render(request, 'comentarios.html')

def Novedades(request):
    if request.method == 'POST':
        NOVEDADES.objects.create(
            text=request.POST.get('text'),
            user=request.user
        )
        messages.success(request, "publicacion exitosa")
        return redirect('/')
    return render(request, 'home.html')
