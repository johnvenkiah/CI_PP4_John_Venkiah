from django import forms
from .models import Ad
from main.categories import category_dict


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
    description = forms.CharField(
        widget=forms.Textarea(
            {
                'rows': 10,
                'class': 'textarea',
            }
        )
    )
    category = forms.ChoiceField(
        choices=zip(category_dict.values(), category_dict.keys()),
        widget=forms.Select(
            attrs={
                'class': 'form-control m-b',
            }
        )
    )
