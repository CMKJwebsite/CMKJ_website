from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse

# Create your views here.


def back_index(request):
    """
    返回index页面
    """
    return render(request, 'index.html')


def check_register_username(request):
    """
    检查注册时用户名是否已经存在
    """
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username).all()
        if user:
            return HttpResponse('1')
        return HttpResponse('0')


def register_user(request):
    """
    注册，写入数据库
    """
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        # make_password_1 = make_password(password_1, 'a', 'pbkdf2_sha1')
        # make_password_2 = make_password(password_2, 'a', 'pbkdf2_sha1')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        verify_code = request.POST.get('verify_code')
        user = User.objects.create_user(username=username, password=password_1, email=email)
        userinfo = UserInfo.objects.create(u_user=user, u_telephone=telephone)
        return redirect('/login')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # username = request.POST['username']
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 利用authenticate实现验证
        user = authenticate(username=username, password=password)
        if user:
            # 验证通过，利用login进行登录
            login(request, user)
            return redirect('/index')
        else:
            error_msg = '用户名或密码错误'
            return render(request, 'login.html', {"error_msg": error_msg})


def logout_user(request):
    logout(request)
    return redirect('/login')
