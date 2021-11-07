<<<<<<< HEAD
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.sitemaps.views import sitemap as sitemap_view
from django.views.decorators.cache import cache_page, never_cache
=======
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView
from django.views.decorators.cache import never_cache
>>>>>>> test-loginform

from . import views

app_name = 'instr_main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
<<<<<<< HEAD
    # path('signup/', views.sign_up, name='signup'),
    path('new/', never_cache(views.AdCreateView.as_view()), name='item-new'),
    path(
        'edit/<int:pk>/',
        never_cache(views.AdUpdateView.as_view()),
        name='ad-edit'
    ),
    path('<int:pk><slug:slug>/', views.AdDetailView.as_view(), name='ad'),
=======
    path('search/', views.SearchView.as_view(), name='search'),
    path('<int:pk><slug:slug>/', views.AdDetailView.as_view(), name='ad'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
>>>>>>> test-loginform
    path(
        'category/<int:pk><slug:slug>/',
        views.CategoryDetail.as_view(),
        name='category'
    ),
<<<<<<< HEAD
    path('search/', views.SearchView.as_view(), name='search'),
    path('user/profile/', views.ProfileView.as_view(), name='profile'),
    path(
        'user/delete/<int:pk>/',
        views.AdDeleteView.as_view(),
        name='delete-ad'
    ),
    path('user/logout/', LogoutView.as_view(), name='logout'),

=======
    path('post_ad/', views.AdCreateView.as_view(), name='post_ad'),
    # path(
    #     'edit/<int:pk>/',
    #     never_cache(views.AdUpdateView.as_view()),
    #     name='ad-edit'
    # ),
    path('delete/<int:pk>/', views.AdDeleteView.as_view(), name='delete-ad'),
    # path('user/logout/', LogoutView.as_view(), name='logout'),
>>>>>>> test-loginform
 ]
