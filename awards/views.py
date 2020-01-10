from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User_profile

# Create your views here.
def index(request):
    people = User_profile.objects.all()
    message = 'This is trying to see whether the app works as required'
    return render(request,'index.html',{'people':people,'message':message})