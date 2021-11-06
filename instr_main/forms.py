from django import forms
from django.utils.translation import ugettext as _

from .models import Ad, Categories, Profile
from .categories import category_dict


class SearchForm(forms.Form):
    # area = forms.ModelChoiceField(
    #     label=_('Area'), queryset=Area.objects.all(), required=False
    # )
    category = forms.ModelChoiceField(
        label=_('Categories'), queryset=Categories.objects.all(), required=False
    )
    query = forms.CharField(required=False, label=_('Query'),)

    def filter_by(self):
        # TODO search using more than one field
        # TODO split query string and make seaprate search by words
        filters = {}
        if self.cleaned_data['category']:
            filters['category'] = self.cleaned_data['category']

        # if self.cleaned_data['area']:
        #     filters['area'] = self.cleaned_data['area']

        filters['description__icontains'] = self.cleaned_data['query']

        return filters


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = (
            'title',
            'category',
            'description',
            'price',
            'image',
            'location',
        )
    description = forms.CharField(widget=forms.Textarea({
        'rows': 10,
        'class': 'textarea',
    }))
    category = forms.ChoiceField(choices=[(v, k) for k, v in category_dict.items()])


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'name',
            'email',
            'username',
            'password',
        )
