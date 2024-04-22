from django.db import models
from businesses.models import *
from main_info.models import MyUser

"""
    this is for all the models for the products and services that are offered by the 
    businesses
"""


# for the products offered
class Product(models.Model):
    productName = models.CharField(max_length= 255, blank= False, null = True)
    units = models.IntegerField(default=1)
    seller = models.ForeignKey(Business, blank=False, on_delete= models.CASCADE)
    price = models.IntegerField(blank= False)
    des = models.TextField(max_length= 200, blank= False, null= False)
    img = models.CharField(max_length=255, null= True)
    color = models.CharField(max_length=255, default= "all")
    cat = models.TextField(max_length= 200, default= "all")
    time_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name
    

# this is for the cart items
class CartItem(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1)


# this is to add favorites 
class Favorites(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
