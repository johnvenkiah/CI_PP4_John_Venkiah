from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.functional import cached_property
from django_google_maps import fields as map_fields
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _
from unidecode import unidecode
from jv_instrumental.settings import DEFAULT_FILE_STORAGE


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(is_active=True)


class Ad(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'Categories', on_delete=models.SET_NULL, null=True
    )
    description = models.CharField(max_length=800)
    image_set = models.ImageField(
        'image', default='placeholder', upload_to=DEFAULT_FILE_STORAGE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=200)
    sold = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)
    is_active = models.BooleanField(_('active'), default=True, db_index=True)

    objects = models.Manager()
    active = ActiveManager()

    def __str__(self):
        if not self.is_active:
            return '[%s] %s' % (_('in active'), self.title)
        return self.title

    class Meta:
        ordering = ['created_on']
        verbose_name = _('ad')
        verbose_name_plural = _('ads')

    def get_absolute_url(self):
        return reverse('django_classified:item', kwargs={
            'pk': self.pk,
            'slug': self.slug
        })

        @cached_property
        def get_keywords(self):
            return ",".join(set(self.description.split()))

        @cached_property
        def image_count(self):
            return self.image_set.count()

        @cached_property
        def featured_image(self):
            return self.image_set.all().first()

        @cached_property
        def related_items(self):
            queryset = Ad.objects \
               .filter(is_active=True) \
               .filter(category=self.category) \
               .exclude(pk=self.pk)
            return queryset

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Ad, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    ads = models.ForeignKey(Ad, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    location = map_fields.AddressField(max_length=200)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.user.username}: Profile'


class Categories(models.Model):
    title = models.CharField('title', max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @cached_property
    def count(self):
        return self.item_set.filter(is_active=True).count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Categories, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'instru_mental:group', kwargs={'pk': self.pk, 'slug': self.slug}
        )
