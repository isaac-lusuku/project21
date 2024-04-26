from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import MyUserSerializer, UserProfileSerializer
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import MyUser, UserProfile
import jwt
import boto3
from django.conf import settings
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
import random

# this creates the user
class CreateUser(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)
    def post(self, request):
        user = request.data
        serializer = MyUserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# this creates the user profile
@api_view(["POST"])
def CreateProfile(request):
    if request.method == "POST":
        data = request.data
        email = data.get("email", None)
        user = MyUser.objects.get(email= email)
        profile = UserProfile.objects.create(
            user = user,
            bio = request.data.get("bio"),
            phone = request.data.get("phone")
        )
        profile.save
        return Response("sorry man", status=status.HTTP_201_CREATED)
    
# this updates the profile image
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

@api_view(["PUT"])
def Upload_image(request):
    file = request.data.get('file')
    user_id = request.data.get('user_id')

    # Retrieve the user profile
    try:
        user_name = MyUser.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(id=user_id)
    except UserProfile.DoesNotExist:
        return Response("User profile does not exist", status=status.HTTP_404_NOT_FOUND)

    # Check if the file exists
    if not file:
        return Response("No file provided", status=status.HTTP_400_BAD_REQUEST)
    
    # Generate a random four-digit number
    random_number = random.randint(1000, 9999)

    # Save the file to S3
    try:
        extension = file.name.split(".")[-1]
        file_name = f"{user_name}.{str(random_number)}.{extension}"
        https_link = upload_image_to_s3(file, file_name)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Update the user profile with the image URL
    serializer = UserProfileSerializer(user_profile, data={"avatar": https_link}, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'url': https_link}, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# this is for serving the user_name, email, contact, bio, avatar
@api_view(['GET'])
def UserInfo(request):
    try:
        id = request.query_params.get("id")
        print(id)
        user_info = MyUser.objects.get(id=id)
        print(user_info)
        profile = UserProfile.objects.get(user = user_info)
        print(profile)
    except MyUser.DoesNotExist:
        raise NotFound("User not found with the specified ID")
    except UserProfile.DoesNotExist:
        raise NotFound("UserProfile not found with the specified ID")

    send_dict = {
        "user_name": user_info.username,  
        "email": user_info.email,
        "phone": profile.phone,
        "bio": profile.bio,
        "avatar_link": profile.avatar
    }
    return Response(send_dict)

