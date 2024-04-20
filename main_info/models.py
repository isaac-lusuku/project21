from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager



# my usermanager
class MyUserManager(BaseUserManager):

    def create_user(self, email, username, password):
        if not email or not username or not password:
            raise ValueError("one of the fields was missing")
        user = self.model(
            email = self.normalize_email(email), 
            username = username
        )
        user.set_password(password)
        user.is_active = True
        user.save()
        return user
    
    def create_superuser(self, email, username, password):
        if not email or not username or not password:
            raise ValueError("one of the fields was missing")
        user = self.model(
            email = self.normalize_email(email), 
        )
        user.username = username
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        user.is_active = True
        return user


# i created a custom user class to overide the defualt one and extend auth functionality
class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=30, blank=False)
    password = models.CharField(max_length=150, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["password", "username"]

    objects = MyUserManager()

    def __str__(self) -> str:
        return self.username
    
    def get_full_name(self):
        '''
        Returns the User name.
        '''
        return self.username


# am to revisit this while setting up the email verification functionality
"""
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
"""

# additional information for the userprofile
class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=255, default="https://i.pinimg.com/736x/87/67/64/8767644bc68a14c50addf8cb2de8c59e.jpg")
    phone = models.CharField(max_length=15, blank=False, null=True)
    bio = models.TextField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.user.username
    

