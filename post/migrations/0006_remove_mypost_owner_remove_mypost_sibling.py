# Generated by Django 4.0.4 on 2022-04-17 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_mypost_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mypost',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='mypost',
            name='sibling',
        ),
    ]
