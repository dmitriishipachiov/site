from django.shortcuts import get_object_or_404, render
from .models import *

app_name = 'lavka'

menu = [{'title': 'Главная', 'url_name': 'lavka:about'}]

def about(request):
    posts = Reklavka.objects.all()
    cats = ReklavkaCategory.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная',
        'cat_selected': 0,
    }
    return render(request, 'lavka/about.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Reklavka, slug=post_slug)
    cats = ReklavkaCategory.objects.all()
    context = {
        'post': post,
        'cats': cats,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id
    }
    return render(request, 'lavka/about.html', context=context)

def show_category(request, cat_id):
    posts = Reklavka.objects.filter(cat_id=cat_id)
    cats = ReklavkaCategory.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'lavka/about.html', context=context)