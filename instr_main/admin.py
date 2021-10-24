from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Ad, Profile


@admin.register(Ad)
class AdAdmin(ModelAdmin):

    list_display = ('title', 'slug', 'price', 'seller', 'created_on', 'sold')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('sold', 'created_on')


@admin.register(Profile)
class AdAdmin(ModelAdmin):

    list_display = ('user', 'slug', 'created_on')
    search_fields = ['user']
    prepopulated_fields = {'slug': ('user',)}
    list_filter = ('user', 'created_on')
