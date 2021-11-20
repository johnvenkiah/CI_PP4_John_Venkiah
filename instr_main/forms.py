from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from .models import Ad, Category, Profile
from .categories import category_dict


class AdForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.attrs.update(
            {
                'required': ''
            }
        )
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


class UserForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].required = True

    class Meta:
        model = User
        # exclude = ('user_ptr_id',)
        fields = (
            'first_name',
            'last_name',
            'email',
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'location',
        )
