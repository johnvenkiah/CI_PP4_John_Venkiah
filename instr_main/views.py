from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView
from django.views import View

import folium
import geocoder

from .forms import AdForm, ProfileForm, UserForm
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

