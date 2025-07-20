from django.contrib import admin
from .models import Profile, Post, Comment, Follow, Like


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'created_at')
    list_filter = ('created_at', 'location')
    search_fields = ('user__username', 'user__email', 'location')
    readonly_fields = ('created_at',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_preview', 'created_at', 'get_like_count', 'get_comment_count')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'content')
    readonly_fields = ('created_at', 'updated_at')

    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content Preview'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'post__content', 'content')
    readonly_fields = ('created_at', 'updated_at')

    def content_preview(self, obj):
        return obj.content[:30] + "..." if len(obj.content) > 30 else obj.content
    content_preview.short_description = 'Content Preview'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('follower__username', 'followed__username')
    readonly_fields = ('created_at',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_object', 'content_type', 'created_at')
    list_filter = ('created_at', 'content_type')
    search_fields = ('user__username',)
    readonly_fields = ('created_at',)
