# Generated by Django 4.0.4 on 2022-04-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_remove_mycategory_myposts'),
        ('post', '0006_remove_mypost_owner_remove_mypost_sibling'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='categories',
            field=models.ManyToManyField(blank=True, to='category.mycategory'),
        ),
    ]
