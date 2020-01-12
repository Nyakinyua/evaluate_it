from django.contrib import admin
from .models import User_profile,Projects,Review,ProjectReview

# Register your models here.
admin.site.register(User_profile)
admin.site.register(Projects)
admin.site.register(ProjectReview)
