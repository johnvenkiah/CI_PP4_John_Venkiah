from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView
from django.views.decorators.cache import never_cache

from . import views

app_name = 'instr_main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('post_ad/', views.AdCreateView.as_view(), name='post_ad'),
    path('<slug:slug>/', views.AdDetailView.as_view(), name='ad_detail'),
    path(
        'category/<int:pk><slug:slug>/',
        views.CategoryDetail.as_view(),
        name='category'
    ),
    # path(
    #     'edit/<int:pk>/',
    #     never_cache(views.AdUpdateView.as_view()),
    #     name='ad-edit'
    # ),
    path('delete/<int:pk>/', views.AdDeleteView.as_view(), name='delete-ad'),
    # path('user/logout/', LogoutView.as_view(), name='logout'),
 ]
