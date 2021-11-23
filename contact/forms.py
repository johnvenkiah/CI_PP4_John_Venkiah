from django import forms


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = True

    name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email Address', max_length=100)
    message = forms.CharField(
                            label='Message',
                            max_length=400,
                            widget=forms.Textarea(
                                {
                                    'rows': 10,
                                    'class': 'textarea',
                                }
                            )
    )

    def __str__(self):
        return f'Email form: {self.email}'
