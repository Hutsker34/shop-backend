from django.db import models
from datetime import datetime

# Create your models here.
class SomeInfo(models.Model):
    cardNumber = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    ccv = models.CharField(max_length=100)

    def __str__(self):
        return f'cardNumber {self.cardNumber}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField(max_length=100, default=0)
    img = models.ImageField(upload_to ='./assets', blank=True, default='./assets/1169.jpg')
    
    def __str__(self):
        return f'Product {self.name}'
    
class Order(models.Model):
    user_email = models.CharField(max_length=100, blank=False, null=False)
    products = models.ManyToManyField('Product', verbose_name='Товары', through='ProductInOrder')
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    total_cost = models.IntegerField(max_length=100, default=0)
    def __str__(self):
        return f'Order {self.user_email} id {self.id}'
    
class ProductInOrder(models.Model):
    product = models.ForeignKey('Product' ,verbose_name='продукт', default=0, 
        on_delete=models.CASCADE)
    order = models.ForeignKey('Order',verbose_name='заказ', default=0,
        on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Количество', default=0)
    
    def __str__(self):
        return f'{self.product.name} x {self.amount}'
    
