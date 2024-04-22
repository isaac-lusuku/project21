from django.contrib import admin
from .models import Business, Service_Business, Selling_Business

class BusinessAdmin(admin.ModelAdmin):
    list_display=('owner', 'name', 'city', 'contact', 'email', 'logo')
admin.site.register(Business, BusinessAdmin)

class SellingBusinessAdmin(admin.ModelAdmin):
    list_display=('business_details', 'category', 'delivery_options', ' customer')
admin.site.register(Selling_Business, SellingBusinessAdmin)

class ServiceBusinessAdmin(admin.ModelAdmin):
    list_display=('business_details', 'category', 'appointment_options', ' customer')
admin.site.register(Service_Business,ServiceBusinessAdmin)