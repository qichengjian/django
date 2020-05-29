from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    # return HttpResponse("Hello World")
    products = [
        Product("Bob"),
        Product("Smith"),
        Product("Tom")
    ]
    return render(request, "index.html", {"products":products})


def new(request):
    return HttpResponse("New Products")
