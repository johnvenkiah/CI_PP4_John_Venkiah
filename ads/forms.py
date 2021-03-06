from django import forms
from .models import Ad
from main.categories import category_dict


class AdForm(forms.ModelForm):
    """
    The ad form, used to create and edit ads by users.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.attrs.update(
            {
                'required': ''
            }
        )
        self.fields['price'].widget.attrs['placeholder'] = '£0.00'

    class Meta:
        model = Ad
        fields = (
            'title',
            'category',
            'description',
            'price',
            'image',
            'location',
            'sold',
        )
    description = forms.CharField(
        widget=forms.Textarea(
            {
                'rows': 10,
                'class': 'textarea',
            }
        )
    )
    category = forms.ChoiceField(
            choices=zip(category_dict.keys(), category_dict.keys()))
