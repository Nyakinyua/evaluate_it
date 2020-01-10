from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
# Create your models here.
class User_profile(models.Model):
    bio = models.CharField(max_length=40)
    profile_pic = ImageField(blank=True,manual_crop="")
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.bio

    # @classmethod
    # def get_profile(cls):
    #     profile =cls.objects.all()
    #     return profile
    