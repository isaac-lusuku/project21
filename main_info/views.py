from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import MyUserSerializer, UserProfileSerializer
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import MyUser, UserProfile
import jwt

# Create your views here.
class CreateUser(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)
    def post(self, request):
        user = request.data
        serializer = MyUserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
        return Response(status=status.HTTP_201_CREATED)