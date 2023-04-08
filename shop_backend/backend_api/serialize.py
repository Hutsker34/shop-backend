from rest_framework import serializers
from .models import SomeInfo, Product


class SomeInfoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SomeInfo
        fields = ['cardNumber', 'name', 'month', 'year', 'ccv']

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = [ 'name', 'cost']