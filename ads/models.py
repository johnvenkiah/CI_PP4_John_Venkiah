from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.functional import cached_property
from django.template.defaultfilters import slugify
from unidecode import unidecode


def user_image_folder(instance, filename):
    return f'static/images/{instance.seller.username}/{filename}'


class Ad(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_image_folder, blank=False)
    category = models.CharField(max_length=250)
    description = models.CharField(max_length=800)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    sold = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'ad'
        verbose_name_plural = 'ads'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Ad, self).save(*args, **kwargs)
