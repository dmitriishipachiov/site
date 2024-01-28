from django.urls import path
from . import views

app_name = 'goroskop'

urlpatterns = [
    path('', views.page, name='page'),
    path('item/<slug:item_slug>/', views.show_post, name='item'),
    path('category/<slug:cat_id>/', views.show_category, name='category')
]
