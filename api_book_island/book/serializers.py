from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Pages, Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    number_of_pages = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ("id", "title", "description", "author", "number_of_pages")
        read_only_fields = ("id", "author", "number_of_pages")
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=('title', 'description'),
                message='Такая книга у тебя уже есть!'
            )
        ]

    def get_number_of_pages(self, obj):
        return get_object_or_404(Book, id=obj.pk).pages.count()


class PagesSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Pages
        fields = ("id", "title", "text", "page", "book", "author")
        read_only_fields = ("id", "book", "author")
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Pages.objects.all(),
                fields=('page', ),
                message='Такая страница уже есть!'
            )
        ]
