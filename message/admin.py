from django.contrib import admin
from .models import Message, MessageNotification


# Register your models here.
admin.site.register(Message)
admin.site.register(MessageNotification)