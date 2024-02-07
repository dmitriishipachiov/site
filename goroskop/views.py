from django.shortcuts import get_object_or_404, render
from .models import *

app_name = 'goroskop'

menu = [{'title': 'Гороскоп', 'url_name': 'goroskop:page'}]


def page(request):
    items = Star.objects.all()
    cats = StarCategory.objects.all()
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
    cats = StarCategory.objects.all()
    context = {
        'item': item,
        'cats': cats,
        'menu': menu,
        'title': item.title,
        'cat_selected': item.cat_id
    }
    return render(request, 'goroskop/page.html', context=context)


def show_category(request, cat_id):
    items = Star.objects.filter(cat_id=cat_id)
    cats = StarCategory.objects.all()
    context = {
        'items': items,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'goroskop/page.html', context=context)
