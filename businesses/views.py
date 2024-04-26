from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import BusinessSerializer
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import Business
import jwt
import boto3
from django.conf import settings
from main_info.models import MyUser
from prods_servs.serializers import ProductSerializer
from prods_servs.models import Product

# this is to create a business
@api_view(["POST"])
def register_business(request):
    id = int(request.data.get("owner"))
    user = MyUser.objects.get(id=id)
    request.data["owner"] = id
    request.data["contact"] =int(request.data.get("contact"))
    print(request.data)
    serializer = BusinessSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        print("in here")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("refused")
        errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


#this is to get all the business info
@api_view(["GET"])
def getBusinessInfo(request):
    id = request.query_params.get("id")
    owner = MyUser.objects.get(id = int(id))
    try:
        business = Business.objects.get(owner = owner)
        serialized_business = BusinessSerializer(business, many=False)
        return Response(serialized_business.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(["GET"])
def getBusinessProducts(request):
    try:
        id = request.query_params.get("id")
        business = Business.objects.get(owner = id)
        products = Product.objects.filter(seller= business)
        serialized_products = ProductSerializer(products, many= True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

