from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='notifications'
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='actor_notifications'
    )
    verb = models.CharField(max_length=255)
    
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.CASCADE, 
        null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('content_type', 'object_id')
    
    timestamp = models.DateTimeField(default=timezone.now) 
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-timestamp']  
    
    def __str__(self):
        return f"{self.actor.username} {self.verb}"
    
    def mark_as_read(self):
        self.is_read = True
        self.save()
