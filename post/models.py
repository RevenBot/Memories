from django.db import models
from category.models import MyCategory
from comments.models import Comments

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/post/img/user_<id>/<filename>
    return 'post/img/post_{0}/{1}'.format(instance.name, filename)

# Create your models here.
class MyPost(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField(max_length=200)
    image=models.ImageField(upload_to=user_directory_path,default='404Image.webp')
    categories=models.ManyToManyField(MyCategory, blank=False,max_length=3)
    comments=models.ManyToManyField(Comments, blank=True)
    created_at = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True,auto_now=True)
    
    