from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from .models import ProductCategory
from django.core import serializers
from django.http import HttpResponse
from utils.json_response import json_response
from utils.response_code import ResponseCode, error_map
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
# Create your views here.


def back_index(request):
    """
    返回index页面
    @param request:
    @return:
    """
    return render(request, 'homepage/index.html')


def view_product(request):
    """
    查看所有产品
    @param request:
    @return:
    """
    products = Product.objects.all()
    if products:
        # json_products = serializers.serialize('json', products)
        # return HttpResponse(json_products, "application/json,charset=utf-8")
        return render(request, 'product/product.html', locals())
    else:
        return json_response(error_number=ResponseCode.NOPRODUCTDATA,
                             error_message=error_map[ResponseCode.NOPRODUCTDATA])


class ProductView(ListView):
    """
    查看所有产品
    """
    template_name = 'product/product.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


def view_product_category(request):
    """
    按照产品分类查看产品
    @param request:
    @return:
    """
    category = request.GET['category']
    # category_obj = ProductCategory.objects.get(c_category_name=category).category_name.all()
    # json_category_obj = serializers.serialize('json', category_obj)
    # category_obj = Product.objects.filter(p_category_name=ProductCategory.objects.get(c_category_name=category))
    # json_category_obj = serializers.serialize('json', category_obj)
    try:
        category_obj = ProductCategory.objects.get(c_category_name=category).category_name.all()
    except ObjectDoesNotExist:
        return json_response(error_number=ResponseCode.NOPRODUCTDATA,
                             error_message=error_map[ResponseCode.NOPRODUCTDATA])
    else:
        # json_category_obj = serializers.serialize('json', category_obj)
        # return HttpResponse(json_category_obj, "application/json")
        return render(request, 'product/product.html', locals())


class ProductCategoryView(ListView):
    """
    按照产品分类查看产品
    """
    template_name = 'product/product.html'
    context_object_name = 'category_obj'

    def get_queryset(self):
        category = self.request.GET['category']
        try:
            return ProductCategory.objects.get(c_category_name=category).category_name.all()
        except ObjectDoesNotExist:
            # return json_response(error_number=ResponseCode.NOPRODUCTDATA,
            #                      error_message=error_map[ResponseCode.NOPRODUCTDATA])
            return {"error_number": ResponseCode.NOPRODUCTDATA, "error_message": error_map[ResponseCode.NOPRODUCTDATA]}


def view_product_detail(request):
    """
    查看某个产品具体详细情况
    @param request:
    @return:
    """
    product_name = request.GET.get('product_name')
    try:
        product_obj = Product.objects.get(p_name=product_name)
    except ObjectDoesNotExist:
        return json_response(error_number=ResponseCode.NOPRODUCTDATA,
                             error_message=error_map[ResponseCode.NOPRODUCTDATA])
    else:
        # dict_product_obj = {'p_name': product_obj.p_name, 'p_details': product_obj.p_details}
        dict_product_obj = model_to_dict(product_obj)
        return render(request, 'product/detail.html', dict_product_obj)
        # json_product_obj = json.dumps(dict_product_obj)
        # return HttpResponse(json_product_obj, "application/json")
