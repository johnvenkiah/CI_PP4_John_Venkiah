from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from .models import Ad, Category, Profile
from .categories import category_dict


class SearchForm(forms.Form):
    # area = forms.ModelChoiceField(
    #     label=_('Area'), queryset=Area.objects.all(), required=False
    # )
    category = forms.ModelChoiceField(
        label=_('Category'), queryset=Category.objects.all(), required=False
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
    # location = forms.CharField(widget=forms.TextInput({
    #     'initial': instance.user.profile.location,
    # }))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'email',
            'location',
        )


# class LocationForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = (
#             'location',
#         )







        # def __init__(self, *args, **kwargs):
        #     super(ProfileForm, self).__init__(*args, **kwargs)
        #     for field_name, field in self.fields.items():
        #         self.fields[field_name].widget.attrs['placeholder'] = User.objects.get(field)

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = User


#     def __init__(self, *args, **kwargs):
#         self.fields['first_name'].widget.attrs['placeholder'] = user.first_name
#         self.fields['last_name'].widget.attrs['placeholder'] = user.last_name
#         self.fields['username'].widget.attrs['placeholder'] = user
#         self.fields['email'].widget.attrs['placeholder'] = user.email
        # super(ProfileForm, self).__init__(*args, **kwargs)
        # # for field in self.fields:
        # #     self.fields[field].widget.attrs.update({'placeholder': getattr(User, field)})





    # def __init__(self, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     u = User
    #     self.fields['first_name'].widget.attrs['placeholder'] = u.first_name
    #     self.fields['last_name'].widget.attrs['placeholder'] = u.last_name
    #     self.fields['username'].widget.attrs['placeholder'] = u.username
    #     self.fields['email'].widget.attrs['placeholder'] = u.email