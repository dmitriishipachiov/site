from django.shortcuts import get_object_or_404, render
from .models import *

menu = [
    {"title": "Сонник", "url_name": ""},
    {"title": "Гороскоп", "url_name": "page"},
    {"title": "Таро", "url_name": "contact"},
    {"title": "Лавка", "url_name": "about"},
]


def contact(request):
    posts = Arkan.objects.all()
    context = {"posts": posts, "menu": menu, "title": "Таро"}
    return render(request, "taro/page.html", context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Arkan, slug=post_slug)
    context = {"post": post, "menu": menu, "title": post.title}

    return render(request, "taro/post.html", context=context)
