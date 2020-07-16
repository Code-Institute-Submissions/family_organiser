from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AcceptedFriendRequests(models.Model):
    from_user = models.ForeignKey(User, related_name="accepted_fromuser", null=True,  on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, null=True, related_name="accepted_touser", on_delete=models.CASCADE)

class FriendRequests(models.Model):
    from_user = models.ForeignKey(User, related_name="fromuser", null=True, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name="owner", null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

    def __str__(self):
        return self.current_user.username

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    profile_image = models.ImageField(null=True, blank=True)
    bio = models.CharField(null=True, max_length=150, default="", blank=True)
    premium = models.BooleanField(default=False)
    status_notification = models.IntegerField(default=0)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.user.username

