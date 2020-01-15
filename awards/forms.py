from django import forms
from .models import *
from pyuploadcare.dj.forms import ImageField
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):
    """
    Form to edit user profile
    """
    class Meta:
        model=User_profile
        fields = ('bio','profile_pic','email','phone_number')

class UpdateProfileForm(forms.ModelForm):
    '''
    Form to add user profile
    '''
    class Meta:
        model = User_profile
        fields = ('bio','profile_pic','email','phone_number')
        
class NewProjectForm(forms.ModelForm):
    '''
    Form that allows user to post new project
    '''
    class Meta:
        model = Projects
        fields = ('title','image','description','project_link') 
        
class ReviewForm(forms.ModelForm):
    """
    Form that allows user post a review for a project
    """
    class Meta:
        model=Review
        exclude = ['project','posted_by']  
        
class RateForm(forms.ModelForm):
    '''
    Form that allows a user to rate a project
    '''
    class Meta:
        model=Rate
        exclude = ['post_rated','user','date']
        
 
    
             
