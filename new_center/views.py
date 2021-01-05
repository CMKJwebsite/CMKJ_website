from django.shortcuts import render

# Create your views here.


def new_center(request):
    return render(request, 'new_center/new_center.html')
