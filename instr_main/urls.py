from django.urls import path
from django.views.decorators.cache import never_cache

from . import views

app_name = 'instr_main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('<slug:user>/', views.ProfileView.as_view(), name='profile'),
 ]
