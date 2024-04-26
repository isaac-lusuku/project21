from django.urls import path
from .views import *


urlpatterns = [
    path('register_business/', register_business),
    path('business_info/', getBusinessInfo),
    path('businessProducts/', getBusinessProducts)
]