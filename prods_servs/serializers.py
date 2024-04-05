from rest_framework import serializers
from .models import Image, Product, Service

class ProdsServSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        field="__all__"
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        field="__all__"
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        field="__all__"

