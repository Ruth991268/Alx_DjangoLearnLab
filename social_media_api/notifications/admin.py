from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['recipient', 'actor', 'verb', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at', 'verb']
    search_fields = ['recipient__username', 'actor__username', 'verb']