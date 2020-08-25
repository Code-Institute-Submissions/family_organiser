# Generated by Django 3.0.7 on 2020-08-24 23:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0005_eventinvite_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='declined',
            field=models.ManyToManyField(blank=True, related_name='event_declined', to=settings.AUTH_USER_MODEL),
        ),
    ]
