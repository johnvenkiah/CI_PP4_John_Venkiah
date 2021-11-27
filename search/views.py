from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q

from .searchlog import searchlog
from ads.models import Ad


def search_view(request):
    ads = Ad.objects.all()
    search = request.GET.get('search')
    category = request.GET.get('select-category')
    area = request.GET.get('select-area')

    if search != '':
        search_string = f'{search}'
    else:
        search_string = 'all Ads'

    if category != '- All Categories -':
        cat_string = f'{category}'
    else:
        cat_string = 'all Categories'

    if area != '- All of Great Britain -':
        area_string = f'{area}'
    else:
        area_string = ' all of Great Britain'

    search_query = f'{search_string} in {cat_string}, {area_string}'

    if search != '' and search is not None:
        ads = ads.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
    if category != '- All Categories -':
        ads = ads.filter(Q(category=category))

    if area != '- All of Great Britain -':
        ads = ads.filter(Q(city=area))

    context = {
        'ads': ads,
        'search_query': search_query,
    }

    return render(request, 'search/search.html', context)


class CategoryDetail(SingleObjectMixin, ListView):
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Ad.objects.all())
        return super(CategoryDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['category'] = self.object
        return context

    def get_queryset(self, **kwargs):
        ad_qs = self.object.ad_set.filter(is_active=True)
        return ad_qs
