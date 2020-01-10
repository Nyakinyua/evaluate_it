from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=50)
    image = ImageField(blank=True,manual_crop="")
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    # class Meta:
    #     ordering = [pub_date]
    
class User_profile(models.Model):
    bio = models.CharField(max_length=40)
    profile_pic = ImageField(blank=True,manual_crop="")
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.bio

