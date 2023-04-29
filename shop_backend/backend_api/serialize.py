from rest_framework import serializers
from .models import SomeInfo, Product, Order, ProductInOrder


class SomeInfoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SomeInfo
        fields = ['cardNumber', 'name', 'month', 'year', 'ccv']

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = [ 'name', 'cost','img']

class OrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Order
        fields = [ 'products', 'user_email' ]

class ProductInOrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductInOrder
        fields = [ 'product', 'order' , 'amount']