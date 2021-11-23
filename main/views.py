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

        coords = [get_lat_long_by_address(item.location) for item in ads]
        area_list = get_city_by_lat_long(coords)
        area_list += ['- All of Great Britain -']
        categories += ['- All Categories -']
        categories = set(categories)

        db = {
            'cat': [
                {
                    'name': category,
                    'url': f'?search=&select-category={category}' +
                    '&select-area=-+All+of+Great+Britain+-',
                    'image': category_dict[category]
                }
                for category in categories if category != '- All Categories -'
            ]
        }

        context = {
            'db': db,
            'categories': sorted(categories),
            'area_list': sorted(set(area_list)),
            'category_dict': category_dict,
        }

        return context
