from django.shortcuts import render
from django.views.generic import ListView
from .models import CaseInfo
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from utils.json_response import json_response
from utils.response_code import ResponseCode, error_map
# Create your views here.


def back_index(request):
    """
    返回index页面
    @param request:
    @return:
    """
    return render(request, 'homepage/index.html')


def view_case(request):
    """
    查看所有案例
    @param request:
    @return:
    """
    cases = CaseInfo.objects.all()
    if cases:
        # json_cases = serializers.serialize('json', cases)
        # return HttpResponse(json_cases, "application/json")
        return render(request, 'case/case.html', locals())
    else:
        return json_response(error_number=ResponseCode.NOCASEDATA,
                             error_message=error_map[ResponseCode.NOCASEDATA])


class CaseView(ListView):
    """
    查看所有案例
    """
    template_name = 'case/case.html'
    context_object_name = 'cases'

    def get_queryset(self):
        return CaseInfo.objects.all()


def view_case_detail(request):
    """
    查看案例详情
    """
    case_name = request.GET.get('case_name')
    try:
        case_obj = CaseInfo.objects.get(c_name=case_name)
    except ObjectDoesNotExist:
        return json_response(error_number=ResponseCode.NOCASEDATA,
                             error_message=error_map[ResponseCode.NOCASEDATA])
    else:
        dict_case_obj = model_to_dict(case_obj)
        return render(request, 'product/detail.html', dict_case_obj)
    # case_obj = Case.objects.filter(c_name=case_name)
    # json_cases = serializers.serialize('json', case_obj)
    # print(case_obj)
    # return HttpResponse(json_cases, "application/json")
