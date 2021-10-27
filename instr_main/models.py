from django.db import models
from django.contrib.auth.models import User
import boto3


class Ad(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    description = models.CharField(max_length=800)
    featured_image = models.ImageField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sold = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: Profile'


class Category(models.Model):
    title = models.CharField('title', max_length=100)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title
