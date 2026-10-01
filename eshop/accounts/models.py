from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    phone=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=500,null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

def save_user_profile(sender,**kwargs):
    if kwargs['created']:
        new_profile=Profile(user=kwargs['instance'])
        new_profile.save()

post_save.connect(receiver=save_user_profile,sender=User)    
