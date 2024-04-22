from django.contrib import admin
from .models import Image, Product, Service

class ImageAdmin(admin.ModelAdmin):
    list_display=('image')
admin.site.register(Image, ImageAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'units', 'seller', 'price', 'description', 'images')
admin.site.register(Product, ProductAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_name', 'provider', 'price', 'description', 'images')