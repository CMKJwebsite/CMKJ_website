from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    返回主页面
    """
    return render(request, "homepage/index.html")

