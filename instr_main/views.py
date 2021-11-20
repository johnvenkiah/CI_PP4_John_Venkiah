from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, FormView
from django.views.generic import ListView, DeleteView, TemplateView
from django.views import generic, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from django.db import IntegrityError
from django.template.defaultfilters import slugify

import folium
import geocoder

from .forms import AdForm, ProfileForm, SearchForm, UserForm
from .models import Ad, Category, Profile
from .categories import category_dict
from jv_instrumental.settings import GOOGLE_API_KEY
from .map_utils import get_lat_long_by_address


class HomeView(TemplateView):
    def get_context_data(self):
        ads = Ad.objects.all()
        coords = [get_lat_long_by_address(item.location) for item in ads]
        area_list = [
            geocoder.google(
                [
                    coord[0], coord[1]
                ], method='reverse'
            ).city for coord in coords
        ]
        context = {
            'category_dict': category_dict,
            'area_list': set(area_list),
        }

        return context

    def get(self, request):
        context = self.get_context_data()
        return render(request, 'instr_main/index.html', context)


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


class ProfileView(ListView):
    model = Ad
    template_name = 'instr_main/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['user_ads'] = Ad.objects.filter(seller=self.request.user)
        context['saved_ads'] = Ad.objects.filter(saved=True)
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy(
            'instr_main:profile', args=[self.kwargs['username']]
        )


@login_required
def edit_profile(request):

    u_form = UserForm(instance=request.user)
    p_form = ProfileForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )

    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, 'Profile Updated Successfully')
        return redirect(
            reverse(
                'instr_main:profile', args=[request.user.username]
            )
        )

    return render(request, 'instr_main/edit_profile.html', context)


class SearchView(ListView):
    model = Ad
    # queryset = Ad.objects.all()
    # paginate_by = 10
    template_name = 'instr_main/search.html'

    # def get_initial(self):
    #     initials = super(SearchView, self).get_initial()
    #     initials['ads'] = Ad.get_for_request(self.request)
    #     return initials


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


# class AdUpdateView(FormsetMixin, UpdateView):
#     is_update_view = True
#     model = Ad
#     form_class = AdForm
#     formset_class = inlineformset_factory(Ad, fields=('file', ))

#     def get_object(self, *args, **kwargs):
#         obj = super(AdUpdateView, self).get_object(*args, **kwargs)
#         if not obj.user == self.request.user and \
#            not self.request.user.is_superuser:
#             raise PermissionDenied
#         return obj

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(AdUpdateView, self).dispatch(*args, **kwargs)


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
