import http
from django.shortcuts import get_object_or_404, render
from .models import *

menu = [
    {'title': 'Сонник', 'url_name': ''},
    {'title': 'Гороскоп', 'url_name': 'page'},
    {'title': 'Таро', 'url_name': 'contact'},
    {'title': 'Лавка', 'url_name': 'about'}
]

def index(request):
    posts = Dream.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Сонник'
    }
    return render(request, 'sonnik/index.html', context=context)

def dreams(request):
    posts = Dream.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Сонник'
    }
    return render(request, 'sonnik/dreams.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Dream, slug = post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title
    }

    return render(request, 'sonnik/post.html', context=context)


def show_category(request, cat_id):
    posts = Dream.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise http(404)

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'рубрики',
        'cat_selected': cat_id
    }
    return render(request, 'sonnik/post.html', context=context)
