# Generated by Django 4.0.1 on 2022-01-07 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectTitle', models.CharField(max_length=100)),
                ('projectDescription', models.CharField(max_length=1500)),
                ('contactDetails', models.CharField(max_length=300)),
                ('pubDate', models.DateTimeField(verbose_name='publication date (of ad ad)')),
                ('projectStartDate', models.DateTimeField(verbose_name='project started (date)')),
            ],
        ),
        migrations.CreateModel(
            name='PresenterAd',
            fields=[
                ('ad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='codermatch.ad')),
            ],
            bases=('codermatch.ad',),
        ),
        migrations.CreateModel(
            name='SupporterAd',
            fields=[
                ('ad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='codermatch.ad')),
            ],
            bases=('codermatch.ad',),
        ),
    ]