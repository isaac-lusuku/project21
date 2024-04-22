from django.contrib import admin
from .models import MyUser, UserProfile

class MyUserAdmin(admin.ModelAdmin):
    list_display=('email', 'username', 'password', 'is_active', 'is_staff ')
admin.site.register(MyUser,MyUserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display=( 'user', 'avatar', 'phone', 'bio', 'is_active', 'date_joined')
admin.site.register(UserProfile, UserProfileAdmin)

