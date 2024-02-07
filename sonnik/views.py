from django.shortcuts import get_object_or_404, render
from .models import *

app_name = 'sonnik'

menu = [{'title': 'Сонник', 'url_name': 'sonnik:index'}]
    
    
def index(request):
    posts = Dream.objects.all()
    cats = DreamCategory.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Сонник',
        'cat_selected': 0,
    }
    return render(request, 'sonnik/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Dream, slug=post_slug)
    cats = DreamCategory.objects.all()
    context = {
        'post': post,
        'cats': cats,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id
    }
    return render(request, 'sonnik/index.html', context=context)
    

def show_category(request, cat_id):
    posts = Dream.objects.filter(cat_id=cat_id)
    cats = DreamCategory.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'sonnik/index.html', context=context)
