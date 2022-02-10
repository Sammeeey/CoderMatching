# Generated by Django 4.0.1 on 2022-02-10 06:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codermatch', '0038_alter_ad_expirationtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='expirationTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 6, 44, 3, 99733, tzinfo=utc), verbose_name='expiration time (of ad)'),
        ),
    ]
