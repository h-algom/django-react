from django.db import models


# Create your models here.
class Message(models.Model):
    # sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sender_notification')
    # recipient = models.ManyToManyField(User)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    received_date = models.DateTimeField(auto_now_add=True)
