from django.db import models



# Create your models here.
class MyCategory(models.Model):
    name=models.CharField(max_length=25,primary_key=True)
    description=models.TextField(max_length=200)
    image=models.ImageField(upload_to='category/img/%Y/%m/%d/',default='404Image.webp')
    
    def __str__(self):
        return self.name