from django.http import JsonResponse
from django.contrib.auth.models import User
from ..models import Post, CommentConsulta

def routes(request):
    routes = [
        'GET /api/posts',
        'GET /api/post/:id'
    ]
    return JsonResponse(routes, safe=False)

def posts(request):
    posts = Post.objects.all()
    posts_dict = []
    for p in posts:
        posts_dict.append({
            'title': p.title,
            'text': p.text
        })
    return JsonResponse(posts_dict, safe=False)

def post(request, id):
    post = Post.objects.get(id=id)
    post_dict = {
        'title': post.title,
        'text': post.text
        }
    return JsonResponse(post_dict, safe=False)

def commentsConsulta(request):
    comentarios = CommentConsulta.objects.all()
    comentarios_dict = []
    for p in comentarios:
        comentarios_dict.append({
                'text': p.text
            }
        )
    return JsonResponse(comentarios_dict, safe=False)


def commentConsulta(request, id):
    comment = CommentConsulta.objects.get(id=id)
    comment_dict = {
        'user': comment.user.username,  # Convertir el campo 'username' del User a JSON serializable
        'text': comment.text
    }
    return JsonResponse(comment_dict, safe=False)