from django import forms


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = True

    class Meta:
        fields = (
            'full_name',
            'email',
            'message',
        )

    message = forms.CharField(
        widget=forms.Textarea(
            {
                'rows': 10,
                'class': 'textarea',
            }
        )
    )
