from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Ad, Profile, Categories


@admin.register(Ad)
class AdAdmin(ModelAdmin):

    list_display = (
        'title', 'slug', 'price', 'seller', 'created_on',
<<<<<<< HEAD
        'sold', 'location', 'category', 'image_set'
=======
        'sold', 'location', 'category', 'image'
>>>>>>> test-loginform
        )
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('sold', 'created_on', )


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):

    list_display = ('user', 'slug', 'created_on')
    search_fields = ['user']
    prepopulated_fields = {'slug': ('user',)}
    list_filter = ('user', 'created_on', )


@admin.register(Categories)
class CategoriesAdmin(ModelAdmin):

    list_display = ('title', )
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', )
