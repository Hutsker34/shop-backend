from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product, SomeInfo, Order, ProductInOrder
from .serialize import SomeInfoSerializer, ProductSerializer , OrderSerializer , ProductInOrderSerializer
from rest_framework.response import Response
from django.db.models import Q
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
                'img': output.img.url,
                'id': output.id
            } for output in Product.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

class ProductDetailView(APIView):
    def get(self, request, product_id):
        
        product = Product.objects.get(id=product_id)

        serializer = ProductSerializer(product)
        return Response(serializer.data)      


        
class OrdersView(APIView):
    def post(self, request):
        # получаем список всех заказов

        email = request.data.get('user_email',"marc32@gmail.com")
        user_orders = Order.objects.filter(user_email=email)
        orders_info = []

        for order in user_orders:
            orders_info.append(order.products)

        # сериализуем и возвращаем данные о всех заказах
        serializer = OrderSerializer(user_orders, many=True)
        return Response(serializer.data)
    


class OrderView(APIView):
    def get(self, request, order_id):
        # получаем список всех заказов
        order = Order.objects.get(id=order_id)


        # сериализуем и возвращаем данные о всех заказах
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def post(self, request):
        # получаем данные о заказе из запроса
        user_email = request.data.get('user_email',"marc32@gmail.com")
        product_ids = request.data.get('product_ids', [])
        amount_array = request.data.get('amount', [])
        order = Order.objects.create(user_email=user_email)
        total_cost = 0 
        for index , value  in enumerate(product_ids):
            product = Product.objects.get(id=value)
            amount = amount_array[index]
            total_cost = total_cost + product.cost
            ProductInOrder.objects.create(product=product, order=order, amount = amount)
        
        order.total_cost = total_cost
        order.save()
        # сериализуем и возвращаем данные о заказе
        serializer = OrderSerializer(order)
        return Response(serializer.data)
        
class ProdectInOrderView(APIView):
    def get(self , request):
        output = [
            {
                'product': output.name,
                'order': output.order,
                'amount': output.amount,
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
    

class ProductsSearchView(APIView):
    
    def post(self, request):
        selected_colors = request.data.get('selectedColors', [])
        selected_types = request.data.get('selectedTypes', [])
        lowPrice = request.data.get('lowPrice', '0')
        highPrice = request.data.get('highPrice', '0')
        searchValue = request.data.get('searchValue', '')
        searchValue = searchValue.strip()

        print('test', highPrice, lowPrice)
        # Построение условий фильтрации

        products = Product.objects.all()
        
        if len(selected_colors) > 0 : 
            filters = Q(color__in=selected_colors) 
            products = products.filter(filters)
        
        if len(selected_types) > 0: 
            filters =  Q(type__in=selected_types)
            products = products.filter(filters)

        if len(searchValue) > 0:
            products = products.filter(name__icontains=searchValue)

        # filterPrice = products.filter(Q(cost__gte=int(lowPrice)) & Q(cost__lte=int(highPrice)))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    