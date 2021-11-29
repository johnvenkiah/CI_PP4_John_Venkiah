from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from jv_instrumental.settings import EMAIL_HOST_USER


class ContactView(FormView):
    template_name = 'contact/contact.html'
    model = User
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        msg1 = f"Mail from {form.cleaned_data['from_email']}\n\n"
        msg2 = '\n\nForm sent from InstruMental through Django'
        cleaned_msg = f'{msg1}{form.cleaned_data["message"]}{msg2}'

        send_mail(
            form.cleaned_data['subject'],
            cleaned_msg,
            form.cleaned_data['from_email'],
            [EMAIL_HOST_USER],
            fail_silently=False
        )

        messages.success(
            self.request, 'Thanks for contacting us, we will reply shortly.'
        )

        return super().form_valid(form)
