# Generated by Django 5.0.1 on 2024-01-03 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
