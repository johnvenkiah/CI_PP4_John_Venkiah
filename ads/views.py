from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect
from search.searchlog import searchlog


from .forms import AdForm
from .models import Ad
from jv_instrumental.settings import GOOGLE_API_KEY


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, slug, *args, **kwargs):
        queryset = Ad.objects.all()
        ad = get_object_or_404(queryset, slug=slug)
        saved = False
        if ad.saved.filter(id=self.request.user.id).exists():
            saved = True

        return render(
            request,
            'ads/ad_detail.html',
            {
                'ad': ad,
                'saved': saved,
            },
        )

class AdSave(View):

    def post(self, request, slug):
        ad = get_object_or_404(Ad, slug=slug)
        print(ad.seller)
        if ad.saved.filter(id=self.request.user.id).exists():
            ad.saved.remove(request.user)
        else:
            ad.saved.add(request.user)

        return HttpResponseRedirect(
            reverse(
                'ads:ad_detail', kwargs={
                    'seller': self.request.user.username,
                    'slug': slug
                }
            )
        )


class AdUpdateView(UpdateView):
    template_name = 'ads/ad_update.html'
    model = Ad
    form_class = AdForm
    google_api_key = GOOGLE_API_KEY

    def get_object(self, *args, **kwargs):
        obj = super(AdUpdateView, self).get_object(*args, **kwargs)
        if not obj.seller == self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super(AdUpdateView, self).get_context_data(**kwargs)
        context['google_api_key'] = self.google_api_key
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AdUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Your Ad is updated')
        return f'/{self.request.user.username}'


class AdCreateView(CreateView):

    is_update_view = False
    model = Ad
    form_class = AdForm
    template_name = 'ads/post_ad.html'
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
        return f'/{self.request.user.username}'


class AdDeleteView(DeleteView):
    model = Ad

    def get_success_url(self, *args, **kwargs):
        messages.success(self.request, 'Your Ad is now deleted')
        return reverse_lazy(
            'user_profile:profile', args=[self.kwargs['seller']]
        )
