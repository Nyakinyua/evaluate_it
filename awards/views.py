from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import User_profile, Projects,Review,ProjectReview
from django.contrib.auth.models import User
from .forms import UpdateProfileForm, NewProjectForm,EditProfileForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import profileSerializer,projectSerializer
from django.contrib.auth import logout
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


# @login_required(login_url="/accounts/login/")
# def single_project(request,project_id):
    
    

@login_required(login_url="/accounts/login/")
def review(request,pk):
    [design,usability,content] = [0],[0],[0]
    
    project = get_object_or_404(Projects,pk=pk)
    profile = User.objects.get(username=request.user)
    current_user = request.user
    print(current_user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        [design,usability,content] = [0],[0],[0]
        
        if form.is_valid()
        form.save()
        rating = Review.objects.last()
        design = rating.design
        usability =rating.usability
        content = rating.content
        rating.post_rated = post
        rating.save()
        
        
    # review = ProjectReview(
    #     design = request.POST['design'],
    #     usability = request.POST['usability'],
    #     content = request.POST['content'],
    #     comment = request.POST['comment'],
    #     user = request.user,
    #     project = project)
    review.save()
    return redirect(request,'rate.html',{'form':form,'project':project,'profile':profile})


@login_required(login_url="/accounts/login/")
def profile(request,user_id):
    try:
        profile = User_profile.objects.get(id=user_id)
        projects = Projects.objects.filter(id=id)
        prof = profile_pic.reverse()[0:1]
    except Exception as e:
        raise Http404()
    
    return render(request,'profile.html',{'profile':profile,'projects':projects})
 
        
@login_required(login_url="/accounts/login/")
def editProfile(request):
    current_user_id=request.user.id
    profile = User_profile.objects.filter(id=current_user_id)
    if len(profile)<1:
        
        if request.method == 'POST':
            form.EditProfileForm(request.POST,request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.id=current_user_id
                profile.save()
            return redirect("profile")
        else:
            form = EditProfileForm()
            return render(request,'edit.html',{'form':form})
    else:
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST,request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                bio = form.cleaned_data['bio']
                profile_pic = form.cleaned_data['profile_pic']
                email = form.cleaned_data['email']
                phone_number = form.cleaned_data['phone_number']
                # update=User_profile.objects.filter(id=current_user_id).update(bio=bio,profile_pic=profile_pic,email=email,phone_number=phone_number)
                profile.save()
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
    
        