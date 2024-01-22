from django.contrib import admin
from .models import *


class ArkanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'descript', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'descript')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Arkan, ArkanAdmin)
