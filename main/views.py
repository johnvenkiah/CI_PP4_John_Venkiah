from django.views.generic import TemplateView
from django.shortcuts import render

from .categories import category_dict
from ads.models import Ad
from .map_utils import get_lat_long_by_address, get_city_by_lat_long


class HomeView(TemplateView):
    def get(self, request):
        context = self.get_context_data()
        return render(request, 'main/index.html', context)

    def get_context_data(self):

        ads = Ad.objects.all()
        categories = [item.category for item in ads]
        categories += ['- All Categories -']
        coords = [get_lat_long_by_address(item.location) for item in ads]
        area_list = get_city_by_lat_long(coords)
        area_list += ['- All of Great Britain -']
        context = {
            'categories': sorted(set(categories)),
            'area_list': sorted(set(area_list)),
            'category_dict': category_dict,
        }

        return context
