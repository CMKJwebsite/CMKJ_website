from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Service
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from utils.json_response import json_response
from utils.response_code import ResponseCode, error_map
from django.forms import model_to_dict
# Create your views here.


def back_index(request):
    """
    返回index页面
    """
    return render(request, 'homepage/index.html')


def view_service(request):
    """
    查看所有行业服务
    """
    services = Service.objects.all()
    # json_services = serializers.serialize('json', services)
    # return HttpResponse(json_services, "application/json")
    return render(request, 'service/service.html', locals())


class ServiceView(ListView):
    """
    查看所有行业服务
    """
    template_name = 'service/service.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.all()


def view_service_detail(request):
    """
    查看服务详情
    """
    service_name = request.GET['service_name']
    try:
        service_obj = Service.objects.get(s_name=service_name)
    except ObjectDoesNotExist:
        return json_response(error_number=ResponseCode.NOSERVICEDATA,
                             error_message=error_map[ResponseCode.NOSERVICEDATA])
    else:
        # dict_service_obj = {'s_name': service_obj.s_name, 's_details': service_obj.s_details}
        dict_service_obj = model_to_dict(service_obj)
        return render(request, 'product/detail.html', dict_service_obj)
