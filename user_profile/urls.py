from django.urls import path

from . import views

app_name = 'user_profile'

urlpatterns = [
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('<slug:user>/', views.ProfileView.as_view(), name='profile'),
 ]
