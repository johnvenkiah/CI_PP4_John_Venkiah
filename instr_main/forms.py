from django import forms
from django.contrib.auth.models import User
from .models import Profile


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
