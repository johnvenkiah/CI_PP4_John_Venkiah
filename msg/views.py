from django.shortcuts import render
from django.views import View
from .models import Msg
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



class MsgView(View):

    def _message(self, user, message, created_on):
        return {
            'message': message,
            'user': user,
            'created_on': created_on,
        }

    def get(self, request):

        context = {
            'sender': self._message('user_1', 'message1', 'created_on1'),
            'recipient': self._message('user_2', 'message2', 'created_on2'),
        }
        return render(request, 'msg/msg.html', context)
    
    @csrf_exempt
    def post(self, request):

        sender = request.user
        message = request.POST.get('message')
        recipient = request.POST.get('recipient')
        created_on = request.POST.get('created_on')

        new_message = Msg(
            sender=sender,
            recipient=recipient,
            message=message,
            created_on=created_on,
        )
        new_message.save()

        context = {
            'sender': self._message(sender, message, created_on)
        }
        return render(request, csrf_exempt('msg/msg.html'), context)
