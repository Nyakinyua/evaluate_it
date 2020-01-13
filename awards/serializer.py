from rest_framework import serializers
from .models import User_profile,Projects
from django.contrib.auth.models import User


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_profile
        fields = ('user','bio','profile_pic','email','phone_number')
        
class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title','image','description','project_link','posted_by','pub_date')