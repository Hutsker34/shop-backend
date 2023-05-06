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
    id = serializers.IntegerField(source='pk', read_only=True) # добавляем поле id
    class Meta: 
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = instance.pk # устанавливаем значение поля id
        return data

class ProductInOrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductInOrder
        fields = [ 'product', 'order' , 'amount']