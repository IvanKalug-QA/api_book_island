from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer


class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        chat = get_object_or_404(Chat, id=self.kwargs['chat_id'])
        serializer.save(author=self.request.user, message=chat)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionError('Чужой пост редактировать нельзя!')
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionError('Чужой пост удалять нельзя!')
        return super().perform_destroy(instance)
