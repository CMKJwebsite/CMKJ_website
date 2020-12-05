from django.shortcuts import render
from .models import Product
from .models import ProductCategory
from django.core import serializers
from django.http import HttpResponse
import json
# Create your views here.


def back_index(request):
    return render(request, 'index.html')


def view_product(request):
    products = Product.objects.all()

    print(products)
    # products_s = serializers.serialize('json', products)
    # products_ss = json.loads(products_s)
    # print(type(products_ss))
    # print(products_ss)
    return render(request, 'product.html', locals())
    # return HttpResponse(products_s, "application/json")


def view_product_category(request):
    category = request.GET['category']
    category_obj = ProductCategory.objects.filter(c_category_name=category).first().id
    # s = Product.objects.filter(id=category_obj)
    print(category_obj)
    # print(type(category_obj))
    # print(s)
    # s = category_obj.
    # product_category = Product.objects.filter(p_category_name=category)
    # json_str = serializers.serialize("json", product_category)
    # json_str = serializers.serialize("json", category_obj)
    # return HttpResponse(json_str)
    return render(request, 'product.html', locals())
