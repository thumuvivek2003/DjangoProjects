from django.contrib import admin
from .models import Room, Message, RoomMember

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at', 'is_private']
    list_filter = ['is_private', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'content', 'timestamp']
    list_filter = ['room', 'timestamp']
    search_fields = ['content', 'user__username']
    readonly_fields = ['timestamp']

@admin.register(RoomMember)
class RoomMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'joined_at', 'is_online']
    list_filter = ['is_online', 'joined_at']
    search_fields = ['user__username', 'room__name']