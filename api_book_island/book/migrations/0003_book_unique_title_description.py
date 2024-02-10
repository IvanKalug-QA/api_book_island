# Generated by Django 4.2.10 on 2024-02-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_pages_unique_page'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'description'), name='unique_title_description'),
        ),
    ]