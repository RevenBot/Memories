from xml.dom.minidom import Comment
from django.db import models

from category.models import MyCategory
from comments.models import Comments


# Create your models here.
class MyPost(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField(max_length=200)
    image=models.ImageField(upload_to='post/img/')
    categories=models.ManyToManyField(MyCategory, blank=True)
    comments=models.ManyToManyField(Comments, blank=True)