from django.shortcuts import render
from django.http import HttpResponse
from .models import Service
from django.core import serializers

# Create your views here.


class DoesNotExist(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


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
    json_services = serializers.serialize('json', services)
    return HttpResponse(json_services, "application/json")
    # return render(request, 'service/service.html', locals())


def view_service_detail(request):
    """
    查看服务详情
    """
    service_name = request.GET['service_name']
    try:
        try:
            service_obj = Service.objects.get(s_name=service_name)
        except Exception:
            raise DoesNotExist('服务不存在')
    except DoesNotExist as e:
        print(e.msg)
        return HttpResponse(e.msg)
    else:
        dict_service_obj = {'s_name': service_obj.s_name, 's_details': service_obj.s_details}
        print(dict_service_obj)
        return render(request, 'product/detail.html', dict_service_obj)
    # case_obj = Case.objects.filter(c_name=case_name)
    # json_cases = serializers.serialize('json', case_obj)
    # print(case_obj)
    # return HttpResponse(json_cases, "application/json")
