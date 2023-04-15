from django.db import models

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
    cost = models.CharField(max_length=100)
    img = models.ImageField(upload_to ='./assets', blank=True, default='./assets/1169.jpg')

    def __str__(self):
        return f'Product {self.name}'
    
class Order(models.Model):
    product = models.ForeignKey('Product', verbose_name='продукт',                                                           
        on_delete=models.CASCADE)
    amount = models.IntegerField( verbose_name='количество', default=0 )
        
    # def __str__(self):
    #     return f'Order {self.}'
    
