from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ('id', 'title', 'author', 'comment_count')
        read_only_fields = ('id', 'author')

    def get_comment_count(self, obj):
        return get_object_or_404(Chat, id=obj.id).messages.count()


class MessageSerializer(serializers.ModelSerializer):
    message = serializers.SlugRelatedField(slug_field='title', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'text', 'author', 'message')
        read_only_fields = ('id', 'author', 'message')
