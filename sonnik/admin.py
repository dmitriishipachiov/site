from django.contrib import admin
from .models import *


class DreamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'descript', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'descript')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Dream, DreamAdmin)
admin.site.register(Category, CategoryAdmin)
