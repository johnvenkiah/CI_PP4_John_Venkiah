from django.urls import path
# from django.views.decorators.cache import never_cache

from . import views

app_name = 'ads'

urlpatterns = [
    path('post_ad/', views.AdCreateView.as_view(), name='post_ad'),
    path(
        'ad_detail/<slug:seller>/<slug:slug>/',
        views.AdDetailView.as_view(),
        name='ad_detail'
    ),
    path(
        'ad_update/<slug:seller>/<slug:slug>/',
        views.AdUpdateView.as_view(), name='ad_update'
    ),
    path(
        'delete/<slug:seller>/<slug:slug>/',
        views.AdDeleteView.as_view(), name='delete_ad'
    ),
 ]
