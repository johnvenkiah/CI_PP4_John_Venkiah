from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Ad(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ads'
    )
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    sold = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
