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
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Сонник',
        'cat_selected': 0,
    }
    return render(request, 'sonnik/index.html', context=context)

def show_post(request, post_slug):
    post = get_object_or_404(Dream, slug = post_slug)
    cats = Category.objects.all()
    context = {
        'post': post,
        'cats': cats,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id
    }
    return render(request, 'sonnik/post.html', context=context)

def show_category(request, cat_id):
    posts = Dream.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'sonnik/index.html', context=context)
