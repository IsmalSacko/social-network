from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ["author", 'body', "created_on"]
    search_fields = ["body", "author__username"]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", 'comment', "created_on"]
    search_fields = ["comment", "author__username"]
    verbose_name_plural = "Comments"

    class Meta:
        model = Comment


admin.site.register(Comment, CommentAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', "birth_date", "location"]
    search_fields = ["user__username", "name", "location"]

    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'date', 'user_has_seen', 'notification_type', ]
    search_fields = ["user__username", "from_user__username"]

    class Meta:
        model = Notification


admin.site.register(Notification, NotificationAdmin)


class ThreadModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'receiver']
    search_fields = ["user__username", "receiver__username"]

    class Meta:
        model = ThreadModel


admin.site.register(ThreadModel, ThreadModelAdmin)


class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['sender_user', 'is_read', 'date']
    search_fields = ["sender_user__username", "receiver_user__username"]

    class Meta:
        model = MessageModel


admin.site.register(MessageModel, MessageModelAdmin)
