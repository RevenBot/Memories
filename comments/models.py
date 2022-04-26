from os import name
from django.db import models



# Create your models here.

class Comments(models.Model):
    comment = models.TextField(max_length=200)
    name=models.CharField(max_length=25,blank=True)
    user = models.ForeignKey("account.Account", on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.comment   