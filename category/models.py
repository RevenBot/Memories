from django.db import models

from post.models import MyPost

# Create your models here.
class MyCategory(models.Model):
    name=models.CharField(max_length=25,primary_key=True)
    description=models.TextField(max_length=200)
    image=models.ImageField(upload_to='category/img/')
    myPosts= models.ManyToManyField(MyPost, related_name='myPosts')
    