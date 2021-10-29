from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.utils.translation import ugettext as alert
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic import ListView, DeleteView, TemplateView
from django.views import generic, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin

from .forms import AdForm, ProfileForm, SearchForm
from .models import Ad, Categories, Profile


class HomeView(View):
    def get(self, request):
        return render(request, "instr_main/index.html")


class FilteredListView(FormMixin, ListView):
    def get_form_kwargs(self):
        return {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            'data': self.request.GET or None
        }

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        form = self.get_form(self.get_form_class())

        if form.is_valid():
            self.object_list = self.object_list.filter(**form.filter_by())

        context = self.get_context_data(form=form)
        return self.render_to_response(context)


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
#         for category in Categories.objects.all():
#             groups = [(group, items_qs.filter(group=group).count()) for group in section.group_set.all()]
#             object_list.append(dict(
#                 section=(section, items_qs.filter(group__section=section).count()),
#                 groups=groups
#             ))

#         context['object_list'] = object_list

#         return context


class ProfileView(UpdateView):
    template_name = 'instru_mental/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('instru_mental:profile')

    def get_queryset(self):
        return Ad.objects.filter(user=self.request.user)

    def get_object(self, queryset=None):
        return Profile.get(self.request.user)

    def form_valid(self, form):
        messages.success(self.request, alert('Profile updated.'))
        return super(ProfileView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)


class SearchView(FilteredListView):
    form_class = SearchForm
    queryset = Ad.objects.all()
    paginate_by = 10
    template_name = 'instru_mental/search.html'

    def get_initial(self):
        initials = super(SearchView, self).get_initial()
        # initials['area'] = Area.get_for_request(self.request)
        return initials


class FormsetMixin(object):
    object = None

    def get(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def get_formset_class(self):
        return self.formset_class

    def get_formset(self, formset_class):
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        if hasattr(self, 'get_success_message'):
            self.get_success_message(form)
        return redirect(self.object.get_absolute_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class CategoryDetail(SingleObjectMixin, ListView):
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Categories.objects.all())
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
    queryset = Ad


class AdUpdateView(FormsetMixin, UpdateView):
    is_update_view = True
    model = Ad
    form_class = AdForm

    def get_object(self, *args, **kwargs):
        obj = super(AdUpdateView, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied
        return obj

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AdUpdateView, self).dispatch(*args, **kwargs)


class AdCreateView(FormsetMixin, CreateView):
    is_update_view = False
    model = Ad
    form_class = AdForm

    def form_valid(self, form, formset):
        form.instance.user = self.request.user
        form.save()

        return super(AdCreateView, self).form_valid(form, formset)

    def get_initial(self):
        initial = super(AdCreateView, self).get_initial()
        # initial['area'] = Area.get_for_request(self.request)
        return initial


class AdDeleteView(DeleteView):
    model = Ad
    success_url = reverse_lazy('instru_mental:user-ads')

    def get_queryset(self):
        queryset = super(AdDeleteView, self).get_queryset()

        if not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)

        return queryset

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AdDeleteView, self).dispatch(*args, **kwargs)


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
