from django.urls import path
from . import views

urlpatterns = [
    path('page/', views.page, name='page'),
    path('item/<slug:item_slug>/', views.show_post, name='item')
]
