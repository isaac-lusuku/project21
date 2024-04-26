from rest_framework import serializers
from .models import  *
from businesses.serializers import BusinessSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = "__all__"

class CombinedSerializer(serializers.Serializer):
    business_data = BusinessSerializer()
    product_data = ProductSerializer()