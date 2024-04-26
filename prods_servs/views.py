from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
import jwt
import boto3
from django.conf import settings
import random
from main_info.models import MyUser
from businesses.models import Business
from rest_framework.exceptions import NotFound
from businesses.serializers import BusinessSerializer


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
    print(request.data)
    print(request.data.get("img").name)
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

    # testing 
    print(request.data)

    # saving the product
    serialized_product = ProductSerializer(data=request.data, partial=True)
    print(serialized_product)
    if serialized_product.is_valid():
        print("is valid")
        serialized_product.save()
        return Response(serialized_product.data, status=status.HTTP_201_CREATED)
    else:
        errors = serialized_product.errors
        print(errors)
        return Response(errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# get all products
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    product_serializer = ProductSerializer(products ,many= True)
    return Response(product_serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def getOne(request):
    try:
        id = int(request.query_params.get("id"))
        product = Product.objects.get(id=id)
        serialzed = ProductSerializer(product, many=False)
        return Response(serialzed.data, status=status.HTTP_200_OK)  # Pass serialized data to Response
    except Product.DoesNotExist:
        return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)  # Return a meaningful error message
    except ValueError:
        return Response({"error": "Invalid ID provided."}, status=status.HTTP_400_BAD_REQUEST)  # Handle invalid ID


@api_view(['GET'])
def getOneFull(request):
    try:
        id = int(request.query_params.get("id"))
        product = Product.objects.get(id=id)
        business = product.seller

        # Serialize individual objects
        serialized_business = BusinessSerializer(business)
        
        return Response(serialized_business.data, status=status.HTTP_200_OK)

    except Product.DoesNotExist:
        return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
    except ValueError:
        return Response({"error": "Invalid ID provided."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_cart(request):
    # Extracting the cart items amd user from the request
    cart_items_data = request.data.get('cartItems', [])
    user_id = request.data.get('id')
    
    # Delete existing cart items for the user
    CartItem.objects.filter(user=user_id).delete()
    
    # Create new cart items from the received data
    created_cart_items = []
    for item_data in cart_items_data:
        item_data['user'] = user_id
        item_data['product'] = item_data.get("id")
        del item_data['id']
        serializer = CartItemSerializer(data=item_data)
        if serializer.is_valid():
            serializer.save()
            created_cart_items.append(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    print(created_cart_items)
    return Response(created_cart_items, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def update_favorites(request):
    # Extracting the favorites items amd user from the request
    favorite_items_data = request.data.get('favorites', [])
    user_id = request.data.get('id')
    
    # Delete existing cart items for the user
    Favorites.objects.filter(user=user_id).delete()
    
    # Create new favorite items from the received data
    created_favorite_items = []
    for item_data in favorite_items_data:
        favorite = {}
        favorite['user'] = user_id
        favorite['product'] = item_data
        serializer = FavoritesSerializer(data=favorite)
        if serializer.is_valid():
            serializer.save()
            created_favorite_items.append(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    print(created_favorite_items)
    return Response(created_favorite_items, status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
def getCart(request):
    user_id = int(request.query_params.get("id"))
    try:
        items = CartItem.objects.filter(user=user_id)
        serialized = CartItemSerializer(items, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return Response("none")
        
@api_view(['GET'])
def getFavorites(request):
    user_id = int(request.query_params.get("id"))
    try:
        items = Favorites.objects.filter(user=user_id)
        serialized = FavoritesSerializer(items, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return Response("none")