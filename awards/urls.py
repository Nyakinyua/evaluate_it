from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search_project,name='search_project'),
    path('new_project/',views.post_project,name='new_project'),
    path('profile/',views.user_profile,name='profile'),
    url(r'^logout/$',views.logout_user,name="logout_user"),
    path('profile/edit/',views.editProfile,name='edit'),
    path('other/',views.other_users,name='others'),
    path('review/<int:id>',views.review,name='review'),
    path('review/rate/<int:id>',views.rate_project,name='rate'),
    url(r'^rate/(?P<project_id>\d+)',views.rate_project, name='rate_project'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    path('api/project/',views.ProjectList.as_view()),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)