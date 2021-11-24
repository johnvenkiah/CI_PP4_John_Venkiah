from django.urls import path

from . import views

app_name = 'user_account'

urlpatterns = [
    path('<int:pk>/delete', views.RemoveAccountView.as_view(), name='remove_account'),
 ]
