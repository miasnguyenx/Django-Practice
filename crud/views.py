from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from crud.models import User, Product, Order
from django import forms
from django.urls import reverse
from .forms import LoginForm
from .forms import RegisterForm, ProductForm
from .helper import vallidatedata

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

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
    product = get_object_or_404(Product, pk=product_code)
    return render(request, 'product/detail.html', {'product': product,'form':ProductForm})

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
                user = User.objects.get(username__contains = username, password__contains = password)
            except Exception as ex:
                print(ex)
                errormessage = ex
                loginform = LoginForm()
                return render(request, 'crud/login.html', {'message': errormessage, 'form': loginform})
            print(user)
            if (user):
                greeting = "hello, welcome home"
                return HttpResponseRedirect('products')
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
                return render(request, 'crud/login.html', {'message': registermessage, 'form': loginform })
    else:
        form = RegisterForm()
        return render(request, 'crud/register.html', {'form': form})
        

# def create(request):
#     orders = Order.objects.all()
#     context = {'orders': orders}
#     return render(request, 'order/index.html', context)
# def orderdetails(request):
    
    
    