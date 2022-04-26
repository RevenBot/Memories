import email
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from post.models import MyPost
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)#quello corrente
    firstname = models.CharField(max_length=100,blank=True)
    surname = models.CharField(max_length=100,blank=True)
    information=models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=100,blank=True)
    mobile = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    posts= models.ManyToManyField(MyPost, related_name='Posts',blank=True)

    
            
