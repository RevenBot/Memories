# Generated by Django 4.0.4 on 2022-04-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_account_posts_account_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='firstname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='surname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
