from django.db import models
from django.contrib.auth.models import User


class Msg(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Message between {self.sender}, {self.recipient}'
