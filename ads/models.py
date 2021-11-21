from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.functional import cached_property
from django.template.defaultfilters import slugify
from unidecode import unidecode


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(is_active=True)


def user_image_folder(instance, filename):
    return f'static/images/{instance.seller.username}/{filename}'


class Ad(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=user_image_folder, blank=False)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True
    )
    description = models.CharField(max_length=800)

    created_on = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    sold = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)
    is_active = models.BooleanField('active', default=True, db_index=True)

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'ad'
        verbose_name_plural = 'ads'

    def __str__(self):
        # if not self.is_active:
        #     return '[%s] %s' % (_('inactive'), self.title)
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Ad, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField('title', max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    @cached_property
    def count(self):
        return self.item_set.filter(is_active=True).count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'instru_mental:category', kwargs={'pk': self.pk, 'slug': self.slug}
        )