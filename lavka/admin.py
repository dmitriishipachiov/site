from django.contrib import admin
from .models import *

class ReklavkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'descript', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'descript')
    prepopulated_fields = {'slug': ('title',)}


class ReklavkaCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Reklavka, ReklavkaAdmin)
admin.site.register(ReklavkaCategory, ReklavkaCategoryAdmin)
