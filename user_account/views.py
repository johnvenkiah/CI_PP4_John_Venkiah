from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from .forms import UserDeleteForm


class RemoveAccountView(DeleteView):
    model = User
    form = UserDeleteForm
    success_url = reverse_lazy('main:home')
    template_name = 'account/remove_account.html'
    success_message = 'Account deleted successfully.'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(RemoveAccountView, self).delete(request, *args, **kwargs)
