from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    phone=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=500,null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
