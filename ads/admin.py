from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Ad


@admin.register(Ad)
class AdAdmin(ModelAdmin):

    list_display = (
        'title', 'slug', 'price', 'seller', 'created_on',
        'sold', 'location', 'category', 'image'
        )

    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('sold', 'created_on', )
