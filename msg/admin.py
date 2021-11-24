from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Msg


@admin.register(Msg)
class MsgAdmin(ModelAdmin):

    list_display = ('sender', 'recipient', 'message',  'created_on',)
    search_fields = ['sender', 'recipient']
    list_filter = ('sender', 'recipient', 'message', 'created_on',)
