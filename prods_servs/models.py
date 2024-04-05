from django.db import models
from businesses.models import *

"""
    this is for all the models for the products and services that are offered by the 
    businesses
"""

# models for the product and service images
class Image(models.Model):
    image = models.ImageField(upload_to='images/')

# for the products offered
class Product(models.Model):
    name = models.CharField(max_length= 30, blank= False)
    units = models.IntegerField(default=1)
    seller = models.ForeignKey(Selling_Business, blank=False, on_delete= models.CASCADE)
    price = models.IntegerField(blank= False)
    description = models.TextField(max_length= 200, blank= False, null= False)
    images = models.ManyToManyField(Image)

    def __str__(self) -> str:
        return self.name
    
# for the services that are offered by the businesses
class Service(models.Model):
    service_name = models.CharField(max_length= 30, blank= False)
    provider = models.ForeignKey(Service_Business, blank=False, on_delete= models.CASCADE, related_name="service_provider")
    price = models.IntegerField(blank= False)
    description = models.TextField(max_length= 200, blank= False, null= False)
    images = models.ManyToManyField(Image)

    def __str__(self) -> str:
        return self.service_name
    