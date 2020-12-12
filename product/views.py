from django.shortcuts import render
from .models import Product
from .models import ProductCategory
from django.core import serializers
from django.http import HttpResponse
import json
# Create your views here.


class DoesNotExist(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


def back_index(request):
    """
    返回index页面
    """
    return render(request, 'index.html')


def view_product(request):
    """
    查看所有产品
    """
    products = Product.objects.all()
    json_products = serializers.serialize('json', products)
    return HttpResponse(json_products, "application/json")
    # return render(request, 'product.html', locals())


def view_product_category(request):
    """
    按照产品分类查看产品
    """
    category = request.GET['category']
    # category_obj = ProductCategory.objects.get(c_category_name=category).category_name.all()
    # json_category_obj = serializers.serialize('json', category_obj)
    # category_obj = Product.objects.filter(p_category_name=ProductCategory.objects.get(c_category_name=category))
    # json_category_obj = serializers.serialize('json', category_obj)
    try:
        try:
            category_obj = ProductCategory.objects.get(c_category_name=category).category_name.all()
        except Exception:
            raise DoesNotExist('该分类下没有产品')
    except DoesNotExist as e:
        print(e.msg)
        return HttpResponse(e.msg)
    else:
        json_category_obj = serializers.serialize('json', category_obj)
        return HttpResponse(json_category_obj, "application/json")
        # return render(request, 'product.html', locals())


def view_product_detail(request):
    """
    查看某个产品具体详细情况
    """
    # product_name = request.GET['product_name']
    # try:
    #     product_obj = Product.objects.filter(p_name=product_name).values('p_name', 'p_details')
    # except ValueError as e:
    #     print(e)
    #     return HttpResponse(e)
    # else:
    #     # print(product_obj)
    #     # json_product_obj = json.dumps(list(product_obj))
    #     # return HttpResponse(json_product_obj, "application/json")
    #     for dict_product_obj in product_obj:
    #         return render(request, 'detail.html', dict_product_obj)
    product_name = request.GET['product_name']
    try:
        try:
            product_obj = Product.objects.get(p_name=product_name)
        except Exception:
            raise DoesNotExist('该产品不存在')
    except DoesNotExist as e:
        print(e.msg)
        return HttpResponse(e.msg)
    else:
        dict_product_obj = {'p_name':product_obj.p_name, 'p_details':product_obj.p_details}
        print(dict_product_obj)
        return render(request, 'detail.html', dict_product_obj)
