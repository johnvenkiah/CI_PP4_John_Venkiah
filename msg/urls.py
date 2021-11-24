from django.urls import path

from . import views

app_name = 'msg'

urlpatterns = [
    path('msg/', views.MsgView.as_view(), name='msg'),
 ]
