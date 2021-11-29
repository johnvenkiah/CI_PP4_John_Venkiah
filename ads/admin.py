# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Internal:
from .models import Ad
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Ad)
class AdAdmin(ModelAdmin):
    """
    the Ad admin class, simple management model for ads
    """

    list_display = (
        'title', 'slug', 'price', 'seller', 'created_on',
        'sold', 'location', 'category', 'image'
        )

    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('sold', 'created_on', )
