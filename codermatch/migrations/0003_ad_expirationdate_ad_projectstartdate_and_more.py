# Generated by Django 4.0.1 on 2022-01-08 07:12

import codermatch.models
import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codermatch', '0002_remove_ad_projectstartdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='expirationDate',
            field=models.DateTimeField(default=codermatch.models.Ad.in30Days, verbose_name='expiration date (of ad)'),
        ),
        migrations.AddField(
            model_name='ad',
            name='projectStartDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='project started (date)'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='pubDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='publication date (of ad ad)'),
        ),
    ]