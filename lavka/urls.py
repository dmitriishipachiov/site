from django.urls import path
from . import views

app_name = 'lavka'

urlpatterns = [
    path('', views.about, name='about'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_id>/', views.show_category, name='category'),
]