from django.contrib import admin
from .models import Status, Comment, CommentNotification, LikeNotification


# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
    )

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'comment',
    )

class CommentNotificationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'status',
    )

class LikeNotificationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'liker',
        'status'
    )


admin.site.register(Status, StatusAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentNotification, CommentNotificationAdmin)
admin.site.register(LikeNotification, LikeNotificationAdmin)