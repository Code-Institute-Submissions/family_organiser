# Generated by Django 3.0.7 on 2020-07-07 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userprofile_bio'),
        ('status', '0003_auto_20200707_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_author_profile', to='user.UserProfile'),
        ),
        migrations.AlterField(
            model_name='status',
            name='comment',
            field=models.ManyToManyField(blank=True, related_name='status_comment', to='status.Comment'),
        ),
    ]
