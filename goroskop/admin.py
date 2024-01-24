from django.contrib import admin
from .models import *


class StarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


class StarCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Star, StarAdmin)
admin.site.register(StarCategory, StarCategoryAdmin)
