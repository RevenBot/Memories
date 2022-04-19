from django.db import models



# Create your models here.

class Comments(models.Model):
    comment = models.TextField(max_length=200)
    user = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment   