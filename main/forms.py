# from django import forms
# from .models import Ad
# from main.categories import category_dict


# class SearchForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['location'].widget.attrs.update(
#             {
#                 'required': ''
#             }
#         )

#     class Meta:
#         model = Ad
#         fields = (
#             'search',
#             'category',
#             'area',
#         )
#     search = forms.CharField(max_length=250)
#     category = forms.ChoiceField(
#             choices=zip(category_dict.keys(), category_dict.keys()))
#     area = forms.ChoiceField(
#             choices=zip(category_dict.keys(), category_dict.keys()))
