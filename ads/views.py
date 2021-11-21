from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin


from .forms import AdForm
from .models import Ad, Category
from jv_instrumental.settings import GOOGLE_API_KEY


class FilteredListView(FormMixin, ListView):
    def get_form_kwargs(self):
        return {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            'data': self.request.GET or None
        }

    def get(self, request, *args, **kwargs):
        self.object_list = self.get.objects.all()

        form = self.get_form(self.get_form_class())

        if form.is_valid():
            self.object_list = self.object_list.filter(**form.filter_by())

        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class SearchView(ListView):
    model = Ad
    template_name = 'instr_main/search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        category = self.request.GET.get('select-category')
        location = self.request.GET.get('select-area')
        context['ads'] = Ad.objects.all()
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy(
            'instr_main:search'
        )


class CategoryDetail(SingleObjectMixin, ListView):
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
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


class AdDetailView(DetailView):
    model = Ad


class AdUpdateView(UpdateView):
    is_update_view = True
    model = Ad
    form_class = AdForm
    formset_class = inlineformset_factory(Ad, fields=('file', ))

    def get_object(self, *args, **kwargs):
        obj = super(AdUpdateView, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user and \
           not self.request.user.is_superuser:
            raise PermissionDenied
        return obj

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AdUpdateView, self).dispatch(*args, **kwargs)


class AdCreateView(CreateView):

    is_update_view = False
    model = Ad
    form_class = AdForm
    template_name = 'instr_main/post_ad.html'
    google_api_key = GOOGLE_API_KEY

    def get_initial(self):
        initial = super(AdCreateView, self).get_initial()
        initial.update(
            {
                'location': self.request.user.profile.location,
            }
        )
        return initial

    def get_context_data(self, **kwargs):
        context = super(AdCreateView, self).get_context_data(**kwargs)
        context['google_api_key'] = self.google_api_key
        return context

    def form_valid(self, form):
        form.instance.seller = self.request.user
        form.save()
        return super(AdCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(AdCreateView, self).form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Your Ad is now posted')
        return '/profile/'


class AdDeleteView(DeleteView):
    model = Ad
    success_url = reverse_lazy('instru_mental:user-ads')

    def get_queryset(self):
        queryset = super(AdDeleteView, self).get.objects.all()

        if not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)

        return queryset

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AdDeleteView, self).dispatch(*args, **kwargs)
