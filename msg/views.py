from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Msg



class InBoxView(View):
    def get(self, request):

        dialog = {
            'recipient': 'John Doe',
            'ad': 'Large Piano',
            'href': 'recipient/sender/',
        }

        dialogs = [
            dialog
        ]

        context = {
            'dialogs': dialogs,
        }
        return render(request, 'msg/inbox.html', context)


class MsgView(View):

    def _message(self, user, message, created_on):
        return {
            'message': message,
            'user': user,
            'created_on': created_on,
        }

    def get(self, request):
        msg = Msg.objects.all()
        
        context = {
            'messages': msg,
            'ad': 'ad',
            'dialog': 'dialog',
        }

        return render(request, 'msg/msg.html', context)

    @csrf_exempt
    def post(self, request):
        sender = request.user
        message = request.POST.get('message')
        recipient = request.POST.get('recipient')
        created_on = datetime.now().strftime('%H:%M, %d %b %Y%Z')

        new_message = Msg(
            sender=sender,
            recipient=recipient,
            message=message,
            created_on=created_on,
        )
        new_message.save()
        msg = Msg.objects.all()

        context = {
            'sender': self._message(sender, message, created_on),
            'messages': msg,
        }
        return render(request, 'msg/msg.html', context)


class InitMsgView(View):
    def post(self, request):
        context = {
            'ad': request.POST.get('ad_slug'),
        }
        print(request.POST)
        return render(request, 'msg/msg.html', context)
