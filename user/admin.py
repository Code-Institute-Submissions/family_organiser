from django.contrib import admin
from .models import Friend, FriendRequests

# Register your models here.
admin.site.register(Friend)
admin.site.register(FriendRequests)