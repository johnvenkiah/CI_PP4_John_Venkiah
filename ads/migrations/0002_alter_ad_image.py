# Generated by Django 3.2.8 on 2021-11-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
