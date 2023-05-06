from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product, SomeInfo, Order, ProductInOrder
from .serialize import SomeInfoSerializer, ProductSerializer , OrderSerializer , ProductInOrderSerializer
from rest_framework.response import Response
import json
# Create your views here.

class SomeInfoView(APIView):
    def get(self , request):
        output = [
            {
                'cardNumber': output.cardNumber,
                'name': output.name,
                'month': output.month,
                'year': output.year,
                'ccv': output.ccv
            } for output in SomeInfo.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = SomeInfoSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class ProductView(APIView):
    def get(self , request):
        output = [
            {
                'name': output.name,
                'cost': output.cost,
                'img': output.img.url
            } for output in Product.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

        
class OrderView(APIView):
    def get(self, request, order_id):
        # получаем список всех заказов
        
        products_in_order = ProductInOrder.objects.filter(order=order_id)
        product_ids = products_in_order.values_list('product', flat=True)
        products = Product.objects.filter(id__in=product_ids)
        
        print('order', products)

        # сериализуем и возвращаем данные о всех заказах
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        # получаем данные о заказе из запроса
        print('req', request.data)
        user_email = request.data.get('user_email',"marc32@gmail.com")
        product_ids = request.data.get('product_ids', [])
        print('email', product_ids)
        # создаем новый объект заказа
        order = Order.objects.create(user_email=user_email)
        
        # добавляем выбранные продукты к заказу
        for product_id in product_ids:
            product = Product.objects.get(id=product_id)
            order.products.add(product)
            # ProductInOrder.objects.create(product=product, order=order)

        # сериализуем и возвращаем данные о заказе
        serializer = OrderSerializer(order)
        return Response(serializer.data)
        
class ProdectInOrderView(APIView):
    def get(self , request):
        output = [
            {
                'product': output.name,
                'order': output.order,
                'amount': output.cost,
            } for output in Order.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        order = ProductInOrderSerializer(data = request.data.order)
        # product_ids = request.POST.getlist('product_ids')
        product_ids = Product.objects.get(name='Продукт 1')
        for product_id in product_ids:
            product = ProductInOrder.objects.create(product=product_id)
            order.products.add(product)

        if product.is_valid(raise_exception=True):
            product.save()
            return Response(product.data)
        