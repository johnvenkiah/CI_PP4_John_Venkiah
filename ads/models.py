from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator

from main.map_utils import get_lat_long_by_address, get_city_by_lat_long


class Ad(models.Model):
    """
    The Ad model, connecting to the User wit the seller fk field.
    """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=False)
    category = models.CharField(max_length=250)
    description = models.CharField(max_length=800)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999999)]
    )
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    sold = models.BooleanField(default=False)
    saved = models.ManyToManyField(User, related_name='ad_saves', blank=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'ad'
        verbose_name_plural = 'ads'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.city:
            coords = [get_lat_long_by_address(self.location)]
            city = (''.join(get_city_by_lat_long(coords)))
            self.city = city
        super(Ad, self).save(*args, **kwargs)
