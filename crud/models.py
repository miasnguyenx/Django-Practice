from django.db import models
import uuid
from faker import Faker
import random
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    
    class Meta:
        ordering = ['created']
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self) -> str:
        return self.user.username
class User(AbstractUser):
    username = models.CharField(max_length=30, default='nameuser', unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(
        default='abc',
        max_length=200,
        )
    def __str__(self) -> str:
        return self.user.username
        
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
    

    
    