from django.urls import path

from . import views

"""
Contact page url
"""

app_name = 'contact'

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
]
