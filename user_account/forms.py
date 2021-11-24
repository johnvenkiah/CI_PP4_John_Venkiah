from django import forms


class UserDeleteForm(forms.Form):
    """
    Simple form that provides a checkbox that signals deletion.
    """
    delete = forms.BooleanField(required=True)
