from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin


from .forms import AdForm
from .models import Ad
from jv_instrumental.settings import GOOGLE_API_KEY


class AdDetailView(DetailView):
    model = Ad


class AdUpdateView(UpdateView):
    pass
    # is_update_view = True
    # model = Ad
    # form_class = AdForm
    # formset_class = inlineformset_factory(Ad, fields=('file', ))

    # def get_object(self, *args, **kwargs):
    #     obj = super(AdUpdateView, self).get_object(*args, **kwargs)
    #     if not obj.user == self.request.user and \
    #        not self.request.user.is_superuser:
    #         raise PermissionDenied
    #     return obj

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(AdUpdateView, self).dispatch(*args, **kwargs)


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
