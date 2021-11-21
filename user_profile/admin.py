from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):

    list_display = ('username', 'created_on', 'location')
    search_fields = ['username']
    list_filter = ('username', 'created_on', 'location')
