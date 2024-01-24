from django.shortcuts import get_object_or_404, render
from .models import *


def contact(request):
    posts = Arkan.objects.all()
    cats = ArkanCategory.objects.all()
    context = {"posts": posts, 'cats': cats, "title": "Таро"}
    return render(request, "taro/contact.html", context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Arkan, slug=post_slug)
    cats = ArkanCategory.objects.all()
    context = {"post": post, 'cats': cats, "title": post.title}

    return render(request, "taro/post.html", context=context)


def show_category(request, cat_id):
    posts = Arkan.objects.filter(cat_id=cat_id)
    cats = ArkanCategory.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'taro/contact.html', context=context)
