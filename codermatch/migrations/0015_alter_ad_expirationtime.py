# Generated by Django 4.0.1 on 2022-01-14 06:42

import codermatch.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codermatch', '0014_remove_ad_expirationdate_ad_expirationtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='expirationTime',
            field=models.DateTimeField(default=codermatch.models.Ad.in30Days, verbose_name='expiration time (of ad)'),
        ),
    ]