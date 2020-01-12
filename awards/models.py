from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

class User_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=40)
    profile_pic = ImageField(blank=True,manual_crop="")
    email = models.EmailField() 
    phone_number = models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        return self.save()
    

class Projects(models.Model):
    title = models.CharField(max_length=50)
    image = ImageField(blank=True,manual_crop="")
    description = models.TextField()
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save_project(self):
        return self.save()
    
    
    @classmethod
    def search_project(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project
        
        
    
    class Meta:
        ordering = ['pub_date']