from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# @receiver(post_save, sender=Profile)
# def update_user(sender, instance, created, **kwargs):
#     parent = instance.username
#     # user = Profile.objects.get(username=parent)
#     parent.first_name = sender.first_name
#     parent.last_name = sender.last_name
#     parent.email = sender.email
#     parent.save()