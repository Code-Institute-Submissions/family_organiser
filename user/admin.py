from django.contrib import admin
from .models import Friend, FriendRequests, UserProfile, AcceptedFriendRequests

# Register your models here.
admin.site.register(Friend)
admin.site.register(FriendRequests)
admin.site.register(UserProfile)
admin.site.register(AcceptedFriendRequests)