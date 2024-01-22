from django.shortcuts import get_object_or_404, render
from .models import *

menu = [
    {'title': 'Сонник', 'url_name': ''},
    {'title': 'Гороскоп', 'url_name': 'index'},
    {'title': 'Таро', 'url_name': 'contact'}
]


def page(request):
    items = Star.objects.all()
    cats = Category.objects.all()
    context = {
        'items': items,
        'cats': cats,
        'menu': menu,
        'title': 'Гороскоп',
        'cat_selected': 0,
    }
    return render(request, 'goroskop/page.html', context=context)


def show_post(request, item_slug):
    item = get_object_or_404(Star, slug = item_slug)
    cats = Category.objects.all()
    context = {
        'item': item,
        'cats': cats,
        'menu': menu,
        'title': item.title,
        'cat_selected': item.cat_id
    }
    return render(request, 'goroskop/item.html', context=context)


def show_category(request, cat_id):
    items = Star.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context = {
        'items': items,
        'cats': cats,
        # 'menu': menu,
        # 'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'goroskop/page.html', context=context)
