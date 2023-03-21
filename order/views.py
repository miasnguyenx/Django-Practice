from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Order

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def details(request):
    return HttpResponse("This is the detail page")

def orders(reqquest):
    return HttpResponse("This is the list order")