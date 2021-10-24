from django.db import models
from django.contrib.auth.models import User
import boto3
# from cloudinary.models import CloudinaryField


class Ad(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ads'
    )
    description = models.TextField()
    featured_image = models.ImageField('image', default='placeholder')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    sold = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='placeholder', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
