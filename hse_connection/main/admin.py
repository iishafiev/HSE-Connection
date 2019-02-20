from django.contrib import admin
from .models import UserProfile, Publication

admin.site.register(UserProfile)
admin.site.register(Publication)