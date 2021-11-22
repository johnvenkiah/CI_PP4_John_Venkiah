from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView

import geocoder

from ads.models import Ad
from .categories import category_dict
from .map_utils import get_lat_long_by_address, get_city_by_lat_long


class HomeView(TemplateView):
    def get_context_data(self):
        ads = Ad.objects.all()
        coords = [get_lat_long_by_address(item.location) for item in ads]
        area_list = get_city_by_lat_long(coords)
        area_list += ['- All of Great Britain -']
        context = {
            'category_dict': category_dict,
            'area_list': sorted(set(area_list)),
        }

        return context

    def get(self, request):
        context = self.get_context_data()
        return render(request, 'main/index.html', context)
