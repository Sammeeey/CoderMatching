# Generated by Django 4.0.1 on 2022-02-01 10:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codermatch', '0029_alter_ad_expirationtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='expirationTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 10, 42, 57, 102793, tzinfo=utc), verbose_name='expiration time (of ad)'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='projectStartDate',
            field=models.DateField(blank=True, null=True, verbose_name='project started (date)'),
        ),
    ]