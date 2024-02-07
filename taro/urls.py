from django.urls import path
from . import views

app_name = 'taro'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('stap/<slug:stap_slug>/', views.show_post, name='stap'),
    path('category/<slug:cat_id>/', views.show_category, name='category')
]
