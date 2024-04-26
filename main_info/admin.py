from django.contrib import admin
from .models import MyUser, UserProfile


admin.site.register(MyUser)
admin.site.register(UserProfile)

