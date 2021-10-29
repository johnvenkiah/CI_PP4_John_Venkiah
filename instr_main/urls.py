from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.sitemaps.views import sitemap as sitemap_view
from django.views.decorators.cache import cache_page, never_cache

from . import views
from .views import HomeView

app_name = 'instr_main'

urlpatterns = [
    path('', HomeView.get_view, name='home'),
    path('new/', never_cache(views.AdCreateView.as_view()), name='item-new'),
    path(
        'edit/<pk>/',
        never_cache(views.AdUpdateView.as_view()),
        name='ad-edit'
    ),
    path(
        '<pk>/',
        views.AdDetailView.as_view(),
        name='ad-detail'
    ),
    path(
        'category/<pk><slug>/',
        views.CategoryDetail.as_view(),
        name='category'
    ),
    path('search/', views.SearchView.as_view(), name='search'),
    path('user/profile/', views.ProfileView.as_view(), name='profile'),
    path(
        'user/delete/<pk/',
        views.AdDeleteView.as_view(),
        name='delete-ad'
    ),
    path('user/logout/', LogoutView.as_view(), name='logout'),

]
