from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from post.models import MyPost
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)#quello corrente
    firstname = models.CharField(max_length=100,blank=True)
    surname = models.CharField(max_length=100,blank=True)
    information=models.CharField(max_length=100,blank=True)
    Posts= models.ManyToManyField(MyPost, related_name='Posts',blank=True)
     
    
    #When user is create we register the account
    # @receiver(post_save, sender=User)
    # def create_user_account(sender, instance, created, **kwargs):
    #     if created:
    #         Account.objects.create(user=instance)
    # #when user is saved/updated we update the account
    # @receiver(post_save, sender=User)
    # def save_user_account(sender, instance, **kwargs):
    #     instance.account.save()
            
