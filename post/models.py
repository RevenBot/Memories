from django.db import models
from django.conf import settings

# Create your models here.
class MyPost(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField(max_length=200)
    image=models.ImageField(upload_to='post/img/')
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    sibling= models.ManyToManyField('self', blank=True)