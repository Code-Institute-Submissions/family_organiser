from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=500, null=True, default="")
    sent_from = models.ForeignKey(User, related_name="messages_sent_from", on_delete=models.CASCADE,  null=True)
    sent_to = models.ForeignKey(User, related_name="messages_sent_to", on_delete=models.CASCADE,  null=True)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
  
    def __str__(self):
        return self.message

class MessageNotification(models.Model):
    user = models.ForeignKey(User, related_name="message_noti_user", null=True, on_delete=models.CASCADE)
    sent_from = models.ForeignKey(User, related_name="message_noti_sent_from", null=True, on_delete=models.CASCADE)
    notifications = models.IntegerField(default=0)

    def __str__(self):
        return self.user