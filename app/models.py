from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user=models.CharField(max_length=10)
    pwd=models.CharField(max_length=10)
    #bjhbm