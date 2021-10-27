from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Ad
from .forms import CommentForm


class AdsList(generic.ListView):
    model = Ad
    queryset = Ad.objects.filter(status=1).order_by('created_on')
    template_name = 'ads_list.html'
    paginate_by = 10  # Posts per page, dj auto adds new page if more posts


class AdDetail(View):

    def display_ad(self, request, slug, *args, **kwargs):
        queryset = Ad.objects.filter(status=1)
        ad = get_object_or_404(queryset, slug=slug)
        saved = False
        if ad.saved.filter(id=self.request.user.id).exists():
            saved = True

        return render(
            request,
            'ad_detail.html',
            {
                'title': ad.title,
                'seller': ad.seller,
                'created_on': ad.created_on,
                'location': ad.location,
                'description': ad.description,
                'image': ad.image,
                'price': ad.price,
                'category': ad.category,
            },
        )

    def post_ad(self, request, slug, *args, **kwargs):
        queryset = Ad.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        saved = False
        if ad.saved.filter(id=self.request.user.id).exists():
            saved = True

        edit_ad_form = EditAdForm(data=request.POST)  # gets data from c-form
        if edit_ad_form.is_valid():
            edit_ad_form.instance.email = request.user.email
            edit_ad_form.instance.name = request.user.username
            ad = edit_ad_form.save(commit=False)
            ad.post = post  # So we know which post has been commented
            ad.save()
        else:
            edit_ad_form = EditAdForm()

        return render(
            request,
            'ad_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))