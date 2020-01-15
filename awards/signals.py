from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import User_profile


@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
  '''
  this is a function that creates a profile of a user after registration
  '''
  if created:
    User_profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
  '''
  this is a fuunction that saves the profile after been made
  '''
  instance.user_profile.save()