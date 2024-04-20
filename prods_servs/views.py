from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import ProductSerializer
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import Product
import jwt
import boto3
from django.conf import settings
import random
from main_info.models import MyUser
from businesses.models import Business
from rest_framework.exceptions import NotFound


# this updates the product image
def upload_image_to_s3(image_file, name):
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    bucket_name = 'group21bucket'
    key = name
    print(name)
    s3.upload_fileobj(image_file, bucket_name, key)
    # Return the URL of the uploaded image
    url = f'https://{bucket_name}.s3.eu-north-1.amazonaws.com/{key}'
    print(url)
    return url


# this is a model to create a product
@api_view(["POST"])
def AddProduct(request):
    image = request.data.get("img")

    # Check if the file exists
    if not image:
        return Response("No file provided", status=status.HTTP_400_BAD_REQUEST)
    
    # Generate a random four-digit number
    random_number = random.randint(1000, 9999)
    
    # Save the file to S3
    try:
        extension = image.name.split(".")[-1]
        prod_name = f'{request.data.get("productName")}.{str(random_number)}'
        file_name = f"{prod_name}.{extension}"
        https_link = upload_image_to_s3(image, file_name)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # adding the image url to request data
    request.data['img'] = https_link

    # saving the product owner business
    user_id = request.data.get("id")
    try:
        user_info = MyUser.objects.get(id=user_id)
        business = Business.objects.get(owner = user_info)
    except MyUser.DoesNotExist:
        raise NotFound("User not found with the specified ID")
    except Business.DoesNotExist:
        raise NotFound("UserProfile not found with the specified ID")
    
    # adding the seller id to the request data
    request.data['seller'] = business.id

    # changing units and price into intergers
    request.data['units'] = int(request.data.get("units"))
    request.data['price'] = int(request.data.get("price"))



