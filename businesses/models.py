from django.db import models
from main_info.models import MyUser
import datetime

# These are the models to handle all the data about businesses

"""
the general model to handle the general information about a business
"""
class Business(models.Model):
    owner = models.ForeignKey(MyUser, blank=True, null= True, on_delete= models.SET_NULL)
    name = models.CharField(max_length= 255, blank=False)
    location = models.CharField(max_length= 250, blank= False)
    email = models.TextField(max_length= 355, blank=True, null=True)
    logo = models.CharField(max_length=255, default="https://i.pinimg.com/originals/92/06/23/92062396ec80ec776743d10db0938789.gif")
    banner = models.CharField(max_length=255, default="https://i.pinimg.com/564x/34/c3/2d/34c32d93468f7527488a188efa30c7e1.jpg")
    contact = models.IntegerField(blank=False, null=True)
    about = models.CharField(max_length=255, blank=False, null=True)
    category = models.TextField(max_length= 255, blank= False, null = False, default="all")
    delivery_options = models.TextField(max_length= 235, blank=True, null=True)
    # customer = models.ManyToManyField(MyUser, blank=True)
    # open_time = models.DateTimeField(default = datetime.time(8, 0))
    # close_time = models.DateTimeField(default = datetime.time(5, 0))

    # is you still have time you can add the business intro video

    def __str__(self) -> str:
        return self.name
    
