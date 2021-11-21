from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
    path(
        'category/<int:pk><slug:slug>/',
        views.CategoryDetail.as_view(),
        name='category'
    ),
 ]
