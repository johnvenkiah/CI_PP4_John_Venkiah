from django import forms


class ContactForm(forms.Form):
    """
    The contact form from which users send emails to the site owner.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = True

    name = forms.CharField(label='Full Name', max_length=100)
    from_email = forms.EmailField(label='Email Address', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)
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
