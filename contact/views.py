# from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User


class ContactView(FormView):
    template_name = 'contact/contact.html'
    model = User
    form_class = ContactForm
    success_url = '/'

    def get_queryset(self):
        self.object = User.objects.get(self.request.user)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        messages.success(self.request, 'Email sent, please await your reply')

        return super().form_valid(form)
