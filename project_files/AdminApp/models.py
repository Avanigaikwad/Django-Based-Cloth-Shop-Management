from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "Category"

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField(default=56)
    #size = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    image1 = models.ImageField(upload_to="images", default="abc.jpg")
    image2 = models.ImageField(upload_to="images", default="abc.jpg")
    image3 = models.ImageField(upload_to="images", default="abc.jpg")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=5)

    class Meta:
        db_table = "Product"

class Payment(models.Model):
    card_no = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)
    expiry = models.CharField(max_length=10)
    balance = models.FloatField(default=0)

    class Meta:
        db_table = "Payment"

