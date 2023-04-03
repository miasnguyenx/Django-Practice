from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from crud.models import User, Product, Order
from django import forms
from django.urls import reverse
from .forms import LoginForm
from .forms import RegisterForm
from .helper import vallidatedata
from django.contrib.auth.hashers import Argon2PasswordHasher
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the main site index.")

def users(request):
    users = User.objects.all()
    context = {'users': users}
    print(type(request))
    print(request)
    return render(request, 'user/index.html', context)


def products(request):
    products = Product.objects.all()
    for product in products:
        price = product.price
        product.price = "$ {:,.2f}".format(price)
    context = {'products': products}
    return render(request, 'product/index.html', context)


def detail(request, product_code):
    print(request.method)
    product = get_object_or_404(Product, pk=product_code)
    print('-------------------------------------')
    print(product)
    print('-------------------------------------')
    return render(request, 'product/detail.html', {'product': product})

def confirm_delete(request, product_code):
    product = get_object_or_404(Product, pk=product_code)
    print('-------------------------------------')
    print(product)
    print('-------------------------------------')
    return render(request, 'product/confirmdelete.html', {'product': product})

def update(request, product_code):
    print(request.method)
    if (request.method == 'POST'):
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['price'])
        print(request.POST['description'])
        name = str(request.POST['name'])
        description = str(request.POST['description'])
        price = str(request.POST['price'])
        product = Product.objects.filter(code = product_code)
        print(product)
        product.update(name=name, description=description, price=price)
        return HttpResponseRedirect(reverse('crud:products'))
    else:
        return HttpResponseRedirect(reverse('crud:products'))
        
def delete(request, product_code):
    print(request.POST)
    if (request.method == 'POST'):
        if request.POST['submit'] == "Confirm":
            print(request.POST)
            product = Product.objects.filter(code = product_code)
            print(product)
            product.delete()
            return HttpResponseRedirect(reverse('crud:products'))
        else:
            return HttpResponseRedirect(reverse('crud:products'))
    else:
        print(request.method)
        return HttpResponseRedirect(reverse('crud:products'))
        

def orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'order/index.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                print(password)
                # password_hash = hash(password)
                user = User.objects.filter(username = username, password = password)
            except Exception as ex:
                print(ex)
                
                errormessage = ex
                loginform = LoginForm()
                return render(request, 'crud/login.html', {'message': errormessage, 'form': loginform})
            if (user):
                greeting = "hello, welcome home"
                login = "logged"
                return HttpResponseRedirect(reverse('crud:products'))
            else:
                errormessage = 'Wrong username or password'
                loginform = LoginForm()
                return render(request, 'crud/login.html', {'message': errormessage, 'form': loginform})
    else:
        form = LoginForm()
    return render(request, 'crud/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                data = form.cleaned_data
                username = data['username']
                password = data['password']
                # password_hash = hash(password)
                firstname = data['first_name']
                lastname = data['last_name']
                email = data['email']

            except Exception as ex:
                print(ex)
                errormessage = ex
                return render(request, 'crud/register.html', {'message': errormessage })
            else:
                user = User.objects.create(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
                registermessage = "register successfully"
                loginform = LoginForm()
                return HttpResponseRedirect(reverse('crud:login'))
    else:
        form = RegisterForm()
        return render(request, 'crud/register.html', {'form': form})

# def create(request):
#     orders = Order.objects.all()
#     context = {'orders': orders}
#     return render(request, 'order/index.html', context)
# def orderdetails(request):
    

    
    