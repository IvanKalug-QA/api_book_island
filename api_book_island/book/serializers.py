from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

from .models import Pages, Book

User = get_user_model()


class PasswordSerializer(serializers.Field):

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        if len(data) < 4:
            raise serializers.ValidationError('Пароль слишком короткий!')
        return make_password(data)


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    number_of_pages = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ("id", "title", "description", "author", "number_of_pages")
        read_only_fields = ("id", "author", "number_of_pages")

    def get_number_of_pages(self, obj):
        return get_object_or_404(Book, id=obj.pk).pages.count()


class PagesSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Pages
        fields = ("id", "title", "text", "page", "book", "author")
        read_only_fields = ("id", "book", "author")


class UserFullSerializer(serializers.ModelSerializer):
    password = PasswordSerializer()

    class Meta:
        model = User
        fields = ("id", "username", "password")
        read_only_fields = ("id", "last_login")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username")
        read_only_fields = ("id", "username")
