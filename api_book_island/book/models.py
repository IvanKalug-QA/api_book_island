from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='book')


class Pages(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголок')
    text = models.TextField(verbose_name='Текст')
    page = models.IntegerField(verbose_name='Страница')
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='pages')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='pages')
