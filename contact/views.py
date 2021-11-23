# from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from jv_instrumental.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_BACKEND



class ContactView(FormView):
    template_name = 'contact/contact.html'
    model = User
    form_class = ContactForm
    success_url = '/'

    # def get_queryset(self):
    #     self.object = User.objects.get(self.request.user)

    def form_valid(self, form):
        # print(self.request.POST)
        # subject = form.subject

        send_mail(
            form.cleaned_data['subject'],
            form.cleaned_data['message'],
            form.cleaned_data['email'],
            [EMAIL_HOST_USER],
            fail_silently=False
            # auth_user=EMAIL_HOST_USER, auth_password=EMAIL_HOST_PASSWORD
        )

        messages.success(self.request, 'Email sent, please await your reply')

        return super().form_valid(form)
