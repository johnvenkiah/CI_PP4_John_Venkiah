from django.urls import path
from django.views.decorators.cache import never_cache

from . import views

app_name = 'ads'

urlpatterns = [
    path('post_ad/', views.AdCreateView.as_view(), name='post_ad'),
    path(
        '<slug:seller>/<slug:slug>/',
        views.AdDetailView.as_view(),
        name='ad_detail'
    ),
    path(
        'edit/<int:pk>/',
        never_cache(views.AdUpdateView.as_view()),
        name='ad-edit'
    ),
    path('delete/<int:pk>/', views.AdDeleteView.as_view(), name='delete-ad'),
 ]
