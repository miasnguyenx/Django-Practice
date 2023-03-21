from django.db import models
import uuid
from faker import Faker
import random

# Create your models here.
    
class Order(models.Model):
    class Status(models.TextChoices):
        cancel = "0", "canceled"
        process = "1", "processing"
        deliver = "2", "delivering"
        complete = "3", "completed"

    status = models.CharField(
        max_length=2,
        choices = Status.choices,
        default = Status.process,
    )
    code = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.code

# class ProductOrder(models.model):
#     Order = models.ForeignKey(Product, on_delete=models.CASCADE)
#     Product = models.ForeignKey(Order, on_delete=models.CASCADE)
    

    
    