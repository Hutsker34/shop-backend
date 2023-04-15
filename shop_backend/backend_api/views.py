from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product, SomeInfo, Order
from .serialize import SomeInfoSerializer, ProductSerializer , OrderSerializer
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
                'product': output.name,
                'amount': output.cost,
            } for output in Order.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)