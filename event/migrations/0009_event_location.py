# Generated by Django 3.0.7 on 2020-09-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20200830_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='No location given', max_length=300),
        ),
    ]