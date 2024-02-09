from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ChatViewSet, MessageViewSet

router = SimpleRouter()

router.register('chats', ChatViewSet)
router.register(r'chats/(?P<chat_id>\d+)/messages',
                MessageViewSet, basename='messages')

urlpatterns = [
    path('v1/', include(router.urls)),
]
