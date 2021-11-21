from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super(Profile, self).save(*args, **kwargs)
