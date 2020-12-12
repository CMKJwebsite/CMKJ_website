from django.shortcuts import render
from .models import Case
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import model_to_dict

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


def view_case(request):
    """
    查看所有案例
    """
    cases = Case.objects.all()
    json_cases = serializers.serialize('json', cases)
    return HttpResponse(json_cases, "application/json")
    # return render(request, 'case.html', locals())


def view_case_detail(request):
    """
    查看案例详情
    """
    case_name = request.GET['case_name']
    try:
        try:
            case_obj = Case.objects.get(c_name=case_name)
        except Exception:
            raise DoesNotExist('案例不存在')
    except DoesNotExist as e:
        print(e.msg)
        return HttpResponse(e.msg)
    else:
        dict_case_obj = model_to_dict(case_obj)
        print(dict_case_obj)
        return render(request, 'detail.html', dict_case_obj)
    # case_obj = Case.objects.filter(c_name=case_name)
    # json_cases = serializers.serialize('json', case_obj)
    # print(case_obj)
    # return HttpResponse(json_cases, "application/json")
