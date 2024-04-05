from rest_framework import serializers
from .models import Business,Selling_Business,Service_Business

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Business
        field="__all__"
class SellingBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Selling_Business
        fields="__all__"
class ServiceBusinnessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service_Business
        fields="__all__"