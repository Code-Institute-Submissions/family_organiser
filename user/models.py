from django.db import models
from django.contrib.auth.models import User

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