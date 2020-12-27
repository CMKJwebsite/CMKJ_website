from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from .models import UserInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from utils.response_code import ResponseCode, error_map
from utils.json_response import json_response
from utils.verify_code import verify_code
from io import BytesIO
import re
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from django.views.generic import TemplateView
from django.views.generic.base import TemplateView
# Create your views here.


def back_index(request):
    """
    return index page
    @param request:
    @return:
    """
    return render(request, 'homepage/index.html')


# def check_register_username(request):
#     """
#     Check username when registering
#     @param request:
#     @return:
#     """
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     if request.method == 'POST':
#         # 获取前端传递的username
#         username = request.POST.get('username', '')
#         # 判断username是否为空
#         if username:
#             # 判断username长度
#             if 2 < len(username) < 16:
#                 regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9_-]{3,15}$')
#                 user_format = regex.search(username)
#                 # username正则匹配
#                 if user_format:
#                     user = User.objects.filter(username=username).exists()
#                     # 判断username是否存在
#                     if not user:
#                         return json_response(error_number=ResponseCode.OK, error_message=error_map[ResponseCode.OK])
#                     else:
#                         return json_response(error_number=ResponseCode.USERNAMEEXIST,
#                                              error_message=error_map[ResponseCode.USERNAMEEXIST])
#                 else:
#                     return json_response(error_number=ResponseCode.USERNAMEFORMAT,
#                                          error_message=error_map[ResponseCode.USERNAMEFORMAT])
#             else:
#                 return json_response(error_number=ResponseCode.USERNAMELENGTH,
#                                      error_message=error_map[ResponseCode.USERNAMELENGTH])
#         else:
#             return json_response(error_number=ResponseCode.USERNAMEEMPTY,
#                                  error_message=error_map[ResponseCode.USERNAMEEMPTY])


# def check_register_email(request):
#     """
#     Check email when registering
#     @param request:
#     @return:
#     """
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     if request.method == 'POST':
#         # 获取前端传递的email
#         email = request.POST.get('email', '')
#         # 判断email是否为空
#         if email:
#             # 验证email格式
#             try:
#                 validate_email(email)
#                 return json_response(error_number=ResponseCode.OK, error_message=error_map[ResponseCode.OK])
#             except ValidationError:
#                 return json_response(error_number=ResponseCode.USEREMAILERROR,
#                                      error_message=error_map[ResponseCode.USEREMAILERROR])
#         else:
#             return json_response(error_number=ResponseCode.USEREMAILEMPTY,
#                                  error_message=error_map[ResponseCode.USEREMAILEMPTY])


# def check_register_telephone(request):
#     """
#     Check telephone when registering
#     @param request:
#     @return:
#     """
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     if request.method == 'POST':
#         # 获取前端传递的telephone
#         telephone = request.POST.get('telephone', '')
#         # 判断telephone是否为空
#         if telephone:
#             # 判断telephone长度
#             if 0 < len(telephone) < 11:
#                 regex = re.compile(r'^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$')
#                 telephone_format = regex.search(telephone)
#                 # telephone正则匹配
#                 if telephone_format:
#                     u_telephone = UserInfo.objects.filter(u_telephone=telephone).exists()
#                     # 判断telephone是否存在
#                     if not u_telephone:
#                         return json_response(error_number=ResponseCode.OK, error_message=error_map[ResponseCode.OK])
#                     return json_response(error_number=ResponseCode.USERTELEPHONEEXIST,
#                                          error_message=error_map[ResponseCode.USERTELEPHONEEXIST])
#                 return json_response(error_number=ResponseCode.USERTELEPHONEERROR,
#                                      error_message=error_map[ResponseCode.USERTELEPHONEERROR])
#             return json_response(error_number=ResponseCode.USERTELEPHONELENGTH,
#                                  error_message=error_map[ResponseCode.USERTELEPHONELENGTH])
#         return json_response(error_number=ResponseCode.USERTELEPHONEEMPTY,
#                              error_message=error_map[ResponseCode.USERTELEPHONEEMPTY])


# def check_register_password(request):
#     """
#     Check password when registering
#     @param request:
#     @return:
#     """
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     if request.method == 'POST':
#         # 获取前端传递的password
#         password = request.POST.get('password', '')
#         # 判断password是否为空
#         if password:
#             # 判断password长度
#             if 6 < len(password) < 16:
#                 regex = re.compile(r'^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$')
#                 password_format = regex.search(password)
#                 # password正则匹配
#                 if password_format:
#                     return json_response(error_number=ResponseCode.OK,
#                                          error_message=error_map[ResponseCode.OK])
#                 return json_response(error_number=ResponseCode.USERPASSWORDERROR,
#                                      error_message=error_map[ResponseCode.USERPASSWORDERROR])
#             return json_response(error_number=ResponseCode.USERPASSWORDLENGTH,
#                                  error_message=error_map[ResponseCode.USERPASSWORDLENGTH])
#         return json_response(error_number=ResponseCode.USERPASSWORDEMPTY,
#                              error_message=error_map[ResponseCode.USERPASSWORDEMPTY])


# def check_re_enter_register_password(request):
#     """
#     Check re-enter password when registering
#     @param request:
#     @return:
#     """
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     if request.method == 'POST':
#         # 获取前端传递的password
#         password = request.POST.get('password', '')
#         # 获取前端传递的re-enter password
#         re_password = request.POST.get('re_password', '')
#         # 判断password是否为空
#         if password:
#             # 判断re-enter password是否为空
#             if re_password:
#                 # 判断re-enter password是否与password一致
#                 encryption_password = make_password(password, 'a', 'pbkdf2_sha1')
#                 encryption_re_password = make_password(re_password, 'a', 'pbkdf2_sha1')
#                 if encryption_password == encryption_re_password:
#                     return json_response(error_number=ResponseCode.OK, error_message=error_map[ResponseCode.OK])
#                 return json_response(error_number=ResponseCode.USERREPASSWORDERROR,
#                                      error_message=error_map[ResponseCode.USERREPASSWORDERROR])
#             return json_response(error_number=ResponseCode.USERREPASSWORDEMPTY,
#                                  error_message=error_map[ResponseCode.USERREPASSWORDEMPTY])
#         return json_response(error_number=ResponseCode.USERPASSWORDEMPTY,
#                              error_message=error_map[ResponseCode.USERPASSWORDEMPTY])


# def get_verification_code_image(request):
#     """
#     获取图片验证码
#     :param request:
#     :return:
#     """
#     # 利用verify_code模块得到img对象和验证码codes
#     img, codes = verify_code()
#     # 直接在内存开辟一点空间存放临时生成的图片
#     buf = BytesIO()
#     img.save(buf, "png")  # 写入内存
#     data = buf.getvalue()  # 从内存中读出
#     request.session['verification_code'] = codes
#     return HttpResponse(data, 'image/png')


# def check_verify_code(request):
#     """
#     检查图片验证码
#     :param request:
#     :return:
#     """
#     verification_code = request.GET.get('verification_code', '')
#     if verification_code:
#         if verification_code.lower() != request.session["verification_code"].lower():
#             return json_response(error_number=ResponseCode.USERVERIFICATIONCODEERROR,
#                                  error_message=error_map[ResponseCode.USERVERIFICATIONCODEERROR])
#         else:
#             return json_response(error_number=ResponseCode.OK, error_message=error_map[ResponseCode.OK])
#     else:
#         return json_response(error_number=ResponseCode.USERVERIFICATIONCODEEMPTY,
#                              error_message=error_map[ResponseCode.USERVERIFICATIONCODEEMPTY])


# def register_user(request):
#     """
#     注册，写入数据库
#     """
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         encryption_password = make_password(password, 'a', 'pbkdf2_sha1')
#         email = request.POST.get('email')
#         telephone = request.POST.get('telephone')
#         user = User.objects.create_user(username=username, password=encryption_password, email=email)
#         UserInfo.objects.create(u_user=user, u_telephone=telephone)
#         return redirect('/login')


# def login_user(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     if request.method == 'POST':
#         # username = request.POST['username']
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # 利用authenticate实现验证
#         user = authenticate(username=username, password=password)
#         if user:
#             # 验证通过，利用login进行登录
#             login(request, user)
#             return redirect('/index')
#         else:
#             error_msg = '用户名或密码错误'
#             return render(request, 'login.html', {"error_msg": error_msg})


# def logout_user(request):
#     logout(request)
#     return redirect('/login')
