# Generated by Django 4.0.4 on 2022-04-17 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
    ]
