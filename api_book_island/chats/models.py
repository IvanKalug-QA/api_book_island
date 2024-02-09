from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='message')
    message = models.ForeignKey(
        'Chat',
        on_delete=models.CASCADE,
        related_name='messages')


class Chat(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chats')
