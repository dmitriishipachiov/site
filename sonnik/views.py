from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render
from .models import *
from django.views.generic import ListView

app_name = 'sonnik'

menu = [{'title': 'Сонник', 'url_name': 'sonnik:index'}]

# class DreamHome(ListView):
#     model = Dream
#     template_name = 'sonnik/index.html'
#     context_object_name = 'posts'

#     def get_queryset(self):
#         return Dream.objects.all().select_related('cat')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = 'Сонник'
#         context["cat_selected"] = 0
#         return context
    
    
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
    return render(request, 'sonnik/post.html', context=context)


# class DreamCategory(ListView):
#     # model = Category
#     template_name = 'sonnik/index.html'
#     context_object_name = 'posts'

#     def get_queryset(self):
#         return Dream.objects.all().select_related('cat')
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cat = context['posts'][0].cat
#         context["title"] = 'Категория - ' + cat.name
#         context["cat_selected"] = cat.pk
#         return context
    

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
