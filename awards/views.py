from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import profileSerializer,projectSerializer
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.

@login_required(login_url="/accounts/login/")
def home(request):
    people = User_profile.objects.all()
    project = Projects.objects.all()
    message = 'This is trying to see whether the app works as required'
    return render(request, 'index.html', {'people': people, 'message': message, 'project': project})


@login_required(login_url="/accounts/login/")
def logout_user(request):
    '''
    view function renders home page once logout
    '''
    
    logout(request)
    return redirect('/')


@login_required(login_url="/accounts/login/")
def post_project(request):
    
    '''
    view function tha renders the post project form
    '''
    if request.method=='POST':
        form=NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)      
            post.posted_by=request.user        
            post.save()
            return redirect('home')
    else:
        title='New_Post'  
        form=NewProjectForm()
        return render(request, 'new_project.html',{"title":title,"form":form})


@login_required(login_url="/accounts/login/")
def search_project(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        results = Projects.search_project(search_term)
        message = f'{search_term} search'

        return render(request, 'search.html', {'message': message, 'results': results, 'search_term': search_term})
    else:
        message = "You did not search any Project, please input project name"
        return render(request, 'search.html', {'message': message})
    
    

@login_required(login_url="/accounts/login/")
def rate_project(request,id):
    [design,usability,content] = [0],[0],[0]
    post = get_object_or_404(Projects,id=project_id)
    current_user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        [design,usability,content] = [[0],[0],[0]]
        
        if form.is_valid():
            form.save()
            rating = Rate.objects.last()
            design = rating.design
            usability = rating.usability
            rating.post_rated = post
            rating.save()
            
            post_ratings =Rate.objects.filter(post_rated=post)
            post_design_ratings = [pr.design for pr in post_ratings]
            design_avg = 0
            for value in post_design_ratings:
                design_avg += value
            design_score = (design_avg/len(post_design_ratings))
            
            
            post_usability_ratings = [pr.usability for pr in post_ratings]
            usability_avg = 0
            for value in post_usability_ratings:
                usability_avg += value
            usability_score = (usability_avg/len(post_usability_ratings))
            
            
            post_content_ratings = [pr.content for pr in post_ratings]
            content_avg = 0
            for value in post_content_ratings:
                content_avg += value
            content_score = (content_avg/len(post_content_ratings))  
        
            score = (design_score +usability_score + content_score)/3
            
            rating.score = score
            rating.save()
            
            score = rating.score
            return redirect('review')
    else:
        form = RateForm()
        return render(request,'index.html',{'user':current_user,'ratings_form':form})




        
@login_required(login_url="/accounts/login/")
def review(request,id):
    """
    view function that renders one post and has a comment section
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by=request.user
            post=Projects.objects.get(id=id)
            comment.project=post
            comment.save()
            return redirect('review',id=id)
    else:
        form = ReviewForm()
        project=Projects.get_one_project(id)  
        project_Id=Projects.get_project_id(id)
        comments=Review.get_review(project_Id)
        return render(request,'one_project.html',{'form':form,'post':project,'comments':comments})
        


@login_required(login_url="/accounts/login/")
def user_profile(request):

    current_user=request.user
    profile = User_profile.objects.filter(user = current_user)
    projects = Projects.objects.filter(posted_by=current_user)
  
   
    
    return render(request,'profile.html',{'profile':profile,'projects':projects})
 
        
@login_required(login_url="/accounts/login/")
def editProfile(request):
    current_user_id=request.user.id
    profexist = User_profile.objects.filter(user = request.user)

    if profexist is None:
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST,request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('profile')
        else:
            
            form = UpdateProfileForm()
            
        return render(request,'edit.html',{'form':form})
    else:
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST,request.FILES,instance = request.user.user_profile)
            if form.is_valid():
                profexist = form.save(commit = False)
                profexist.user = request.user
                profexist.save()
                return redirect('profile')
            else:
                messages.info(request,'al fields are required')
                return redirect('profile')
        else:
            form = UpdateProfileForm()
            return render(request,'edit.html',{'form':form})
                
    
    
    
@login_required(login_url="/accounts/login/")
def other_users(request,user_id):
    try:
        profile_image = User_profile.objects.filter(id=user_id).all()
        profile = profile_pic.reverse()[0:1]
        projects = Projects.objects.filter(id=user_id)
        users = User.objects.filter(id=user_id).all()
    except Exception as e:
        raise Http404()
    return render(request,'other.html',{'users':users,'profile':profile,'projects':projects})


class ProfileList(APIView):
    def get(self,request,format=None):
        all_profile = User_profile.objects.all()
        serializers = profileSerializer(all_profile,many=True)
        return Response(serializers.data)
    
class ProjectList(APIView):
    def get(self,request,format=None):
        all_projects = Projects.objects.all()
        serializers = projectSerializer(all_projects,many=True)
        return Response(serializers.data)
    
        