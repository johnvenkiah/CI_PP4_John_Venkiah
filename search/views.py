from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.db.models import Q
from .searchlog import searchlog
from ads.models import Ad


def SearchView(request):
    ads = Ad.objects.all()
    search = request.GET.get('search')
    category = request.GET.get('select-category')
    area = request.GET.get('select-area')

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
    }

    searchlog.search_log = request.get_full_path()
    print('SEARCHLOG: ', searchlog.search_log)

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
        # area = Area.get_for_request(self.request)
        # if area:
        #     return item_qs.filter(area=area)
        return ad_qs
