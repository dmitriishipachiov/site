from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('post/<slug:post_slug>/', views.show_post, name='post')
]
