from django.shortcuts import render
from .models import Product
from .models import ProductCategory
from django.core import serializers
from django.http import HttpResponse
# Create your views here.


def back_index(request):
    return render(request, 'index.html')


def view_product(request):
    products = Product.objects.all()
    json_products = serializers.serialize('json', products)
    return HttpResponse(json_products, "application/json")
    # return render(request, 'product.html', locals())


def view_product_category(request):
    category = request.GET['category']
    # category_obj = ProductCategory.objects.get(c_category_name=category).category_name.all()
    # json_category_obj = serializers.serialize('json', category_obj)
    # category_obj = Product.objects.filter(p_category_name=ProductCategory.objects.get(c_category_name=category))
    # json_category_obj = serializers.serialize('json', category_obj)
    category_obj = ProductCategory.objects.get(c_category_name=category).category_name.all()
    json_category_obj = serializers.serialize('json', category_obj)
    return HttpResponse(json_category_obj, "application/json")
    # return render(request, 'product.html', locals())


def view_product_detail(request):
    product_name = request.GET['product_name']
    product_obj = Product.objects.filter(p_name=product_name).all()
    json_product_obj = serializers.serialize('json', product_obj)
    return HttpResponse(json_product_obj, "application/json")
