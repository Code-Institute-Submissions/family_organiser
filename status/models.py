from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.
class Status(models.Model):
    user = models.ForeignKey(User , related_name="status_creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=350)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    likes = models.IntegerField(null=True, blank=True)
    liked_by = models.ManyToManyField(User, related_name="liked_users")
    liked_by_usernames = models.ArrayField()
    image = models.ImageField(null=True, blank=True)