from django.urls import path
from . import views

app_name = 'sonnik'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_id>/', views.show_category, name='category'),
]
