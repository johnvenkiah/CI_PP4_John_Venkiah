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

# class BaseView(View):
#     def get_context_data(self):
#         profile = self.request.user.Profile
#         context = {
#             'profile': profile,
#         }

#         return context

#     def get(self, request):
#         context = self.get_context_data()
#         return render(request, 'instr_main/base.html', context)


class HomeView(TemplateView):
    def get_context_data(self):
        # profile = None
        # if self.request.user != 'AnonymousUser':
        #     profile = self.request.user.profile
        area_list = ['here', 'there', 'everywhere']
        context = {
            'category_dict': category_dict,
            'area_list': area_list,
            # 'profile': profile,
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


# ---------------------GAMMALT UNDER---------------------------------


# class CategoryListView(TemplateView):
#     template_name = 'instru_mental/category_list.html'

#     def get_context_data(self, **kwargs):
#         context = super(CategoryListView, self).get_context_data(**kwargs)

#         ad_qs = Ad.active
#         # area = Area.get_for_request(self.request)
#         # if area:
#         #     ad_qs = ad_qs.filter(area=area)

#         object_list = []
#         # Prepare list of tuples with object/count
#         for category in Category.objects.all():
#             groups = [(group, items_qs.filter(group=group).count()) for group in section.group_set.all()]
#             object_list.append(dict(
#                 section=(section, items_qs.filter(group__section=section).count()),
#                 groups=groups
#             ))

#         context['object_list'] = object_list

#         return context

# ---------------------GAMMALT OVAN ___________________________________


class ProfileView(ListView):
    model = Ad
    template_name = 'instr_main/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['user_ads'] = Ad.objects.filter(seller=self.request.user)
        context['saved_ads'] = Ad.objects.filter(saved=True)
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('instr_main:profile', args=[self.kwargs['username']])


# class EditProfileView(UpdateView):
#     form_class = UserForm
#     template_name = 'instr_main/edit_profile.html'
#     model = User
#     # success_url = reverse('instr_main:profile')

#     # def get_success_url(self, *args, **kwargs):
#     #     return reverse_lazy('instr_main:profile')

#     def form_valid(self, form):
#         user = form.save(commit=True)
#         user.save()
#         messages.success(self.request, 'User info saved')
#         return HttpResponseRedirect(reverse('instr_main:profile', args=[user.username]))
#         # return redirect('profile', slug=user.username)
    
#     def form_invalid(self, form):
#         return super(EditProfileView, self).form_invalid(form)

#     def get_object(self):
#         return self.request.user


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
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, 'Your Profile has been Updated Successfully')
        return redirect(reverse('instr_main:profile', args=[request.user.username]))

    return render(request, 'instr_main/edit_profile.html', context)


class SearchView(FilteredListView, ListView):
    form_class = SearchForm
    queryset = Ad.objects.all()
    paginate_by = 10
    template_name = 'instru_mental/search.html'

    def get_initial(self):
        initials = super(SearchView, self).get_initial()
        # initials['area'] = Area.get_for_request(self.request)
        return initials


# class FormsetMixin(object):
#     object = None

#     def get(self, request, *args, **kwargs):
#         if getattr(self, 'is_update_view', False):
#             self.object = self.get_object()
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         formset_class = self.get_formset_class()
#         formset = self.get_formset(formset_class)
#         return self.render_to_response(self.get_context_data(form=form, formset=formset))

#     def post(self, request, *args, **kwargs):
#         if getattr(self, 'is_update_view', False):
#             self.object = self.get_object()
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         formset_class = self.get_formset_class()
#         formset = self.get_formset(formset_class)
#         if form.is_valid() and formset.is_valid():
#             return self.form_valid(form, formset)
#         else:
#             return self.form_invalid(form, formset)

#     def get_formset_class(self):
#         return self.formset_class

#     def get_formset(self, formset_class):
#         return formset_class(**self.get_formset_kwargs())

#     def get_formset_kwargs(self):
#         kwargs = {
#             'instance': self.object
#         }
#         if self.request.method in ('POST', 'PUT'):
#             kwargs.update({
#                 'data': self.request.POST,
#                 'files': self.request.FILES,
#             })
#         return kwargs

#     def form_valid(self, form, formset):
#         self.object = form.save()
#         formset.instance = self.object
#         formset.save()
#         if hasattr(self, 'get_success_message'):
#             self.get_success_message(form)
#         return redirect(self.object.get_absolute_url())

#     def form_invalid(self, form, formset):
#         return self.render_to_response(self.get_context_data(form=form, formset=formset))


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
    # def get_queryset(self):
    #     return get_object_or_404(
    #         Ad, slug=self.kwargs['slug']
    #     )

    # def get_absolute_url(self):
    #     return reverse('instr_main:ad_detail', args=[(self.slug)])
# class AdDetail(View):
#     # model = Ad

#     def get(self, request, slug, *args, **kwargs):
#         queryset = Ad.objects.filter(seller=self.request.user)
#         ad = get_object_or_404(queryset, slug=slug)
#         saved = False
#         if ad.saved.filter(id=self.request.user.id).exists():
#             saved = True

#         return render(
#             request,
#             'ad_detail.html',
#             {
#                 'ad': ad,
#                 'saved': saved,
#             },
#         )

# class AdUpdateView(FormsetMixin, UpdateView):
#     is_update_view = True
#     model = Ad
#     form_class = AdForm
#     formset_class = inlineformset_factory(Ad, fields=('file', ))

#     def get_object(self, *args, **kwargs):
#         obj = super(AdUpdateView, self).get_object(*args, **kwargs)
#         if not obj.user == self.request.user and not self.request.user.is_superuser:
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

    def get_initial(self):
        initial = super(AdCreateView, self).get_initial()
        initial.update(
            {
                'location': self.request.user.profile.location,
            }
        )
        return initial

    def form_valid(self, form):
        form.instance.seller = self.request.user
        form.save()
        return super(AdCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(AdCreateView, self).form_invalid(form)

    def get_success_url(self):
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



# ____________________GAMMALT__________________________________

#______________________________________________________________

# class AdsList(generic.ListView):
#     model = Ad
#     queryset = Ad.objects.filter(status=1).order_by('created_on')
#     template_name = 'ads_list.html'
#     paginate_by = 10  # Posts per page, dj auto adds new page if more posts


# class AdDetail(View):

#     def display_ad(self, request, slug, *args, **kwargs):
#         queryset = Ad.objects.filter(status=1)
#         ad = get_object_or_404(queryset, slug=slug)
#         saved = False
#         if ad.saved.filter(id=self.request.user.id).exists():
#             saved = True

#         return render(
#             request,
#             'ad_detail.html',
#             {
#                 'title': ad.title,
#                 'seller': ad.seller,
#                 'created_on': ad.created_on,
#                 'location': ad.location,
#                 'description': ad.description,
#                 'image': ad.image,
#                 'price': ad.price,
#                 'category': ad.category,
#             },
#         )

#     def post_ad(self, request, slug, *args, **kwargs):
#         queryset = Ad.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         saved = False
#         if ad.saved.filter(id=self.request.user.id).exists():
#             saved = True

#         edit_ad_form = EditAdForm(data=request.POST)  # gets data from c-form
#         if edit_ad_form.is_valid():
#             edit_ad_form.instance.email = request.user.email
#             edit_ad_form.instance.name = request.user.username
#             ad = edit_ad_form.save(commit=False)
#             ad.post = post  # So we know which post has been commented
#             ad.save()
#         else:
#             edit_ad_form = EditAdForm()

#         return render(
#             request,
#             'ad_detail.html',
#             {
#                 'post': post,
#                 'comments': comments,
#                 'commented': True,
#                 'liked': liked,
#                 'comment_form': CommentForm()
#             },
#         )


# class PostLike(View):

#     def post(self, request, slug):
#         post = get_object_or_404(Post, slug=slug)

#         if post.likes.filter(id=self.request.user.id).exists():
#             post.likes.remove(request.user)
#         else:
#             post.likes.add(request.user)

#         return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# ------------------CONTEXTS.PY #

# from .models import Profile


# def base_context(request):
#     print('user: ', request.user)
#     if request.user.is_authenticated:
#         user = request.user
#         profile = Profile.objects.get(username=user)
#     else:
#         profile = None
#     context = {
#         'profile': profile,
#     }

#     return context
