from rest_framework import serializers
from core.message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content', "is_read"]
        read_only_field = ['is_read']
