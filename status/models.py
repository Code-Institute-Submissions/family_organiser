from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(User, related_name="comment_author", on_delete=models.CASCADE)
    author_profile = models.ForeignKey(UserProfile, related_name="comment_author_profile",null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

class Status(models.Model):
    user = models.ForeignKey(User , related_name="status_creator", on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, related_name="status_user_profile",null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=350)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    likes = models.IntegerField(null=True, blank=True)
    liked_by = models.ManyToManyField(User, blank=True, related_name="liked_users")
    image = models.ImageField(null=True, blank=True)
    comment = models.ManyToManyField(Comment, related_name="status_comment",  blank=True)

