from django.shortcuts import get_object_or_404, render
from .models import *

app_name = 'taro'

menu = [{'title': 'Таро', 'url_name': 'taro:contact'}]


def contact(request):
    staps = Arkan.objects.all()
    cats = ArkanCategory.objects.all()
    context = {"staps": staps, 'cats': cats, 'menu': menu, "title": "Таро"}
    return render(request, "taro/contact.html", context=context)


def show_post(request, stap_slug):
    stap = get_object_or_404(Arkan, slug = stap_slug)
    cats = ArkanCategory.objects.all()
    context = {"stap": stap, 'cats': cats, 'menu': menu, "title": stap.title}
    return render(request, "taro/contact.html", context=context)


def show_category(request, cat_id):
    staps = Arkan.objects.filter(cat_id=cat_id)
    cats = ArkanCategory.objects.all()
    context = {'staps': staps, 'cats': cats, 'menu': menu, 'title': 'Отображение по рубрикам', 'cat_selected': cat_id}
    return render(request, 'taro/contact.html', context=context)
