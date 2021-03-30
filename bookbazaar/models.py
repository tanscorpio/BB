from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    boughtby = models.CharField(max_length=30,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True ,blank=True )   

class OrderItem(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True ,blank=True )
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,null=True,blank=True)

class Order(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True ,blank=True )
    orderitem = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()

class SellItem(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True ,blank=True )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    sold_date = models.DateTimeField(auto_now_add=True)