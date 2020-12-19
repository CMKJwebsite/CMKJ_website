from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from utils.response_code import ResponseCode, error_map
from utils.json_response import json_response
import re

# Create your views here.


def back_index(request):
    """
    返回index页面
    @param request:
    @return:
    """
    return render(request, 'index.html')


def check_register_username(request):
    """
    检查注册时用户名
    @param request:
    @return:
    """
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        if username:
            if 2 < len(username) < 16:
                regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9_-]{3,15}$')
                user_format = regex.search(username)
                if user_format:
                    user = User.objects.filter(username=username).all()
                    if user:
                        return json_response(error_number=ResponseCode.OK, error_message=error_map[ResponseCode.OK])
                    return json_response(error_number=ResponseCode.USERNAMEEXIST,
                                         error_message=error_map[ResponseCode.USERNAMEEXIST])
                else:
                    return json_response(error_number=ResponseCode.USERNAMEFORMAT,
                                         error_message=error_map[ResponseCode.USERNAMEFORMAT])
            else:
                return json_response(error_number=ResponseCode.USERNAMELENGTH,
                                     error_message=error_map[ResponseCode.USERNAMELENGTH])
        else:
            return json_response(error_number=ResponseCode.USERNAMEEMPTY,
                                 error_message=error_map[ResponseCode.USERNAMEEMPTY])


def check_register_email(request):
    """
    检查注册时邮箱格式是否正确
    @param request:
    @return:
    """
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        email = request.POST.get('email', '')
        if email:
            try:
                validate_email(email)
                return json_response(error_number=ResponseCode.OK, error_message=error_map[ResponseCode.OK])
            except ValidationError:
                return json_response(error_number=ResponseCode.USEREMAILERROR,
                                     error_message=error_map[ResponseCode.USEREMAILERROR])
        else:
            return json_response(error_number=ResponseCode.USEREMAILEMPTY,
                                 error_message=error_map[ResponseCode.USEREMAILEMPTY])


def check_register_telephone(request):
    """
    检查注册时电话号码格式是否正确
    """
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        telephone = request.POST.get('telephone')
        u_telephone = UserInfo.objects.filter().all()
        if u_telephone:
            return json_response(error_number=ResponseCode.OK, error_message=error_map[ResponseCode.OK])
        else:
            return json_response(error_number=ResponseCode.USERTELEPHONEERROR,
                                 error_message=error_map[ResponseCode.USERTELEPHONEERROR])


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
