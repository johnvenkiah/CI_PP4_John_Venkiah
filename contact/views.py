# from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        messages.success(self.request, 'Email sent, please await your reply')

        return super().form_valid(form)

    def get_queryset(self):
        self.object = User(instance=self.request.user)
