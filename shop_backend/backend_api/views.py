from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from .serialize import SomeInfoSerializer, ProductSerializer
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
                # 'img': output.img
            } for output in Product.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)