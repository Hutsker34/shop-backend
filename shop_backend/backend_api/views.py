from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product, SomeInfo, Order, ProductInOrder
from .serialize import SomeInfoSerializer, ProductSerializer , OrderSerializer , ProductInOrderSerializer
from rest_framework.response import Response
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
    def get(self , request):
        output = [
            {
                'products': output.name,
                'user_email': output.email,
            } for output in Order.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        
        product_ids = request.data.get('product_ids', [])
        print('idsss',product_ids)
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
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
        order = ProductInOrderSerializer(data = request.data.email)
        product_ids = request.POST.getlist('product_ids')
        print('idsss',product_ids)
        for product_id in product_ids:
            product = ProductInOrder.objects.create(product=product_id)
            order.products.add(product)

        if product.is_valid(raise_exception=True):
            product.save()
            return Response(product.data)
        