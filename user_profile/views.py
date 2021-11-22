from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import BaseDetailView
from django.contrib.auth.models import User

from braces.views import SelectRelatedMixin

from .forms import ProfileForm, UserForm
from ads.models import Ad
from user_profile.models import Profile
from jv_instrumental.settings import GOOGLE_API_KEY


class ProfileView(TemplateView, BaseDetailView, SelectRelatedMixin):
    model = User
    template_name = 'user_profile/profile.html'
    select_related = ('profile',)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return self.get_queryset().get(username=self.kwargs['user'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.get_object()
        context['user_ads'] = Ad.objects.filter(seller=self.get_object())
        context['saved_ads'] = Ad.objects.filter(saved=True)
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy(
            'instr_main:profile', args=[self.kwargs['username']]


    # def get_context_data(self, **kwargs):
    #     context = super(ProfileView, self).get_context_data(**kwargs)
    #     context['user_ads'] = Ad.objects.filter(seller=self.request.user)
    #     context['saved_ads'] = Ad.objects.filter(saved=True)
    #     context['user'] = self.get_object()
    #     return context
        )
    # model = Ad
    # template_name = 'user_profile/profile.html'
    # select_related = ('profile')

    # def get_object(self):
    #     return self.get_queryset().get(user=self.kwargs['username'])



@login_required
def edit_profile(request):

    u_form = UserForm(instance=request.user)
    p_form = ProfileForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'google_api_key': GOOGLE_API_KEY,
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
                'user_profile:profile', args=[request.user.username]
            )
        )

    return render(request, 'user_profile/edit_profile.html', context)