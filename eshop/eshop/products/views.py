# coding=utf-8
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product


def index(request):
    product = Paginator(Product.objects.all(), 2).page(request.GET.get('page',1))


    return render(request, 'index.html', { 'products' : product } )