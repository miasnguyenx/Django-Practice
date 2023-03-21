from django.db import models
import uuid
from faker import Faker
import random
from django import forms

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, default='nameuser')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(
        default='abc',
        max_length=50,
        )

class Product(models.Model):
    code = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         null=False,
         editable = False)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# return "%s %s %d" % a_name, a_desc, a_price
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    code = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    products = models.ManyToManyField(Product)
    
    # def __str__(self):
    #     return self.code

# class ProductOrder(models.model):
#     Order = models.ForeignKey(Product, on_delete=models.CASCADE)
#     Product = models.ForeignKey(Order, on_delete=models.CASCADE)
    

    
    