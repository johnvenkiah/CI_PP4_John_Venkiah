from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Msg
from ads.models import Ad



class InBoxView(View):
    def get(self, request):
        user = request.user
        dialogs = Msg.objects.filter(sender=user)

        context = {
            'dialogs': dialogs,
        }
        return render(request, 'msg/inbox.html', context)


class MsgRedundantView(View):

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


class MsgView(View):

    def _message(self, user, message, created_on):
        return {
            'message': message,
            'user': user,
            'created_on': created_on,
        }

    def get(self, request):
        ad = request.POST.get('ad_slug')
        msg = Msg.objects.filter(ad=ad)
        
        context = {
            'messages': msg,
            'ad': ad,
        }

        return render(request, 'msg/msg.html', context)

    @csrf_exempt
    def post(self, request):
        sender = request.user
        message = request.POST.get('message')
        created_on = datetime.now().strftime('%H:%M, %d %b %Y%Z')
        ad = request.POST.get('ad_slug'),
        recipient = Ad.objects.filter(slug=ad)

        new_message = Msg(
            sender=sender,
            recipient=recipient,
            message=message,
            created_on=created_on,
            ad=ad,
        )

        new_message.save()
        msg = Msg.objects.filter(ad=ad)
        context = {
            'ad': ad,
            'sender': self._message(sender, message, created_on),
            'messages': msg,
        }
        return render(request, 'msg/msg.html', context)
