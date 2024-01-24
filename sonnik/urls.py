from django.urls import path
from . import views

urlpatterns = [
    path('', views.DreamHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]
