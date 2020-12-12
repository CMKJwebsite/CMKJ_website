from django.shortcuts import render

# Create your views here.


def back_index(request):
    """
    返回index页面
    """
    return render(request, 'index.html')


def about(request):
    """
    查看about页面
    """
    return render(request, 'about.html')
