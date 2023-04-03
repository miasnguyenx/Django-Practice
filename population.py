import os
import django
from django.contrib.auth.hashers import make_password, check_password
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproject.settings')
django.setup()

## FAKE POP SCRIPT

import random
from crud.models import Product, User
from crud.models import Order as CrudOrder
from faker import Faker
from order.models import Order as OrderOrder
from django.contrib.auth import authenticate
import uuid

fakegen = Faker()

def add_product(n=10):
    for i in range(n):
        name = fakegen.name()
        text = fakegen.text(90)
        code = uuid.uuid4()
        price = random.randrange(100000, 1000000, 10000)
        p = Product.objects.get_or_create(name=name, description=text, price=price)[0]
        p.save()
        
def add_user(n=10):
    for i in range(n):
        firstname = fakegen.first_name()
        lastname = fakegen.last_name()
        email = fakegen.email()
        u = User.objects.get_or_create(first_name = firstname, last_name = lastname, email = email)[0]
        u.save()

def add_order(n=10):
    for i in range(n):
        name = fakegen.name()
        o = OrderOrder.objects.get_or_create(name=name)[0]

def add_order_clone(n=10):
    for i in range(n):
        o = CrudOrder.objects.create()
        
def add_password():
        password = make_password('haha')
        check = check_password('haha', password)
        return print(password, check)
    
def add_order_product(n=10):
    for i in range(n):
        # o1 = CrudOrder();
        # o1.save()
        code = 'a6752801a0b74f5da4e6beb61e9a85aa'
        uuid_code = uuid.UUID(code)
        print(type(uuid_code))
        p1 = Product.objects.filter(code=uuid_code)
        print(p1)
        p2 = Product.objects.filter(code="a6752801a0b74f5da4e6beb61e9a85aa")
        print(p2)
        p3 = Product.objects.filter(name__contains='Patricia Hayes')
        print(p3)
    
if __name__ == '__main__':
    print("populating script!")
    # add_order_product(1)
    add_password()
    print("complete")
    
    
    