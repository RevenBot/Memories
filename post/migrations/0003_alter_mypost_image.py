# Generated by Django 4.0.4 on 2022-04-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_mypost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='image',
            field=models.ImageField(upload_to='post/static/post/img/'),
        ),
    ]