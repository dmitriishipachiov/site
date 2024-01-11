from django.shortcuts import get_object_or_404, render
from .models import *

menu = [
    {'title': 'Сонник', 'url_name': ''},
    {'title': 'Гороскоп', 'url_name': 'page'},
    {'title': 'Таро', 'url_name': 'contact'},
    {'title': 'Лавка', 'url_name': 'about'}
]


def page(request):
    items = Star.objects.all()
    context = {
        'items': items,
        'menu': menu,
        'title': 'Гороскоп'
    }
    return render(request, 'goroskop/page.html', context=context)


def show_post(request, item_slug):
    item = get_object_or_404(Star, slug = item_slug)
    context = {
        'item': item,
        'menu': menu,
        'title': item.title
    }
    return render(request, 'goroskop/item.html', context=context)
