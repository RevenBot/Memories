from django.db import models

# Create your models here.
class MyCategory(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField(max_length=200)
    image=models.ImageField(upload_to='category/img/')
    