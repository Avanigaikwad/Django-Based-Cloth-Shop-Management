from django.db import models
from AdminApp.models import Product,Category
from datetime import datetime

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=20)
    
    class Meta:
        db_table = "UserInfo"

class Address(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    addr = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=6)
    mobile = models.IntegerField(default=10)
    name = models.ForeignKey(UserInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = "Address"

class MyCart(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.CharField(max_length=3)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = "MyCart"

class MyWishlist(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        db_table = "MyWishlist"

class OrderData(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    date = models.DateField(default = datetime.now)
    amount = models.FloatField(default=0)
    details = models.CharField(max_length=5000)

    class Meta:
        db_table = "OrderData"