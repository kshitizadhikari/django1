# Generated by Django 5.0.6 on 2024-05-22 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
