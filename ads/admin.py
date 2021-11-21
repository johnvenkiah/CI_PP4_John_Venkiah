from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Ad, Category


@admin.register(Ad)
class AdAdmin(ModelAdmin):

    list_display = (
        'title', 'slug', 'price', 'seller', 'created_on',
        'sold', 'location', 'category', 'image'
        )
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('sold', 'created_on', )


@admin.register(Category)
class CategoryAdmin(ModelAdmin):

    list_display = ('title', )
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', )
