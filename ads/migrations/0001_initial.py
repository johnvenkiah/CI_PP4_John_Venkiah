# Generated by Django 3.2.8 on 2021-11-21 19:51

import ads.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to=ads.models.user_image_folder)),
                ('category', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=800)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('sold', models.BooleanField(default=False)),
                ('saved', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ad',
                'verbose_name_plural': 'ads',
                'ordering': ['-created_on'],
            },
        ),
    ]