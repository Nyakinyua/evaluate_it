from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.

class User_profile(models.Model):
    """
    class that creates an instance of a user profile
    """
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
    """
    class that creates instance of a project
    """
    title = models.CharField(max_length=50)
    image = ImageField(blank=True,manual_crop="")
    description = models.TextField()
    project_link = models.URLField(max_length=250,default=None)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save_project(self):
        return self.save()
    
    def delete_project(self):
        proj = Projects.objects.all().delete()
        return proj
    
    '''
    method to search for projects
    '''
    @classmethod
    def search_project(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project
        
        
    
    class Meta:
        ordering = ['pub_date']
        
class Rate(models.Model):
    RATING_CHOICES = ((1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'),(6,'six'),(7,'seven'),(8,'eight'),(9,'nine'),(10,'ten'))
    design = models.PositiveSmallIntegerField('Rating(stars)',blank=False,default=0,choices=RATING_CHOICES)
    usability = models.PositiveSmallIntegerField('Rating(stars)',blank=False,default=0,choices=RATING_CHOICES)
    content = models.PositiveSmallIntegerField('Rating(stars)',blank=False,default=0,choices=RATING_CHOICES)
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        abstract = True   
        
class Review(models.Model):
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)   
    comment = models.TextField()
    posted_by = models.ForeignKey(User,default=None,on_delete=models.CASCADE)