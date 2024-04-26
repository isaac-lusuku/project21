from django.urls import path
from .views import *


urlpatterns = [
    path('addProduct/', AddProduct),
    path('getProducts/', getProducts),
    path('getOne/', getOne),
    path('updatecart/', update_cart),
    path('updatefavorites/', update_favorites),
    path('getCart/', getCart),
    path('getFavorites', getFavorites),
    path('getOneFull/', getOneFull)
]