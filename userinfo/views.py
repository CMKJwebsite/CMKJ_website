from django.shortcuts import render

# Create your views here.


def back_index(request):
    """
    返回index页面
    """
    return render(request, 'index.html')
