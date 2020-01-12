from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search_project,name='search_project'),
    path('new_project/',views.post_project,name='new_project'),
    path('profile/<int:user_id>',views.profile,name='profile'),
    url(r'^logout/$',views.logout_user,name="logout_user"),
    path('profile/edit',views.editProfile,name='edit'),
    path('other/',views.other_users,name='others'),
    path('review/',views.review,name=review)
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)