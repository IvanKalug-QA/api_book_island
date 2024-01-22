from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Pages, Book
from .serializers import (BookSerializer, PagesSerializer,
                          UserFullSerializer, UserSerializer)

User = get_user_model()


class UpdataDeletePerformMixin:
    def get_book(self):
        return get_object_or_404(Book, id=self.kwargs.get('book_id'))

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Доступ запрещен!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Доступ запрещен!')
        super().perform_destroy(instance)


class BookViewSet(UpdataDeletePerformMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PagesViewSet(UpdataDeletePerformMixin, ModelViewSet):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, book=self.get_book())

    def get_queryset(self):
        return self.get_book().pages.all().order_by('page')

    def get_object(self):
        page = get_object_or_404(self.get_queryset(),
                                 page=self.kwargs.get('pk'))
        return page


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        if self.action == 'retrieve':
            if self.get_object().username != self.request.user.username:
                return UserSerializer
            return UserFullSerializer
        return UserFullSerializer

    def perform_update(self, serializer):
        if serializer.instance.username != self.request.user.username:
            raise PermissionDenied('Доступ запрещен!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.username != self.request.user.username:
            raise PermissionDenied('Доступ запрещен!')
        super().perform_destroy(instance)