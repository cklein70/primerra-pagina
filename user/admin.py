from django.contrib import admin
from user.models import UserProfile

@admin.register(UserProfile)
class UserProfileAdamin(admin.ModelAdmin):
    list_display= ("phone", "birth_date")

 
