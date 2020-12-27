from django.http import JsonResponse
from .response_code import ResponseCode


def json_response(error_number=ResponseCode, error_message='', data=None, **kwargs):
    """
    该方法实现的目的是为了使json数据在传输过程中,能够携带错误代码之类的信息
    :param error_number: 错误代码
    :param error_message: 错误信息
    :param data: 携带的用户信息数据,例如用户名,手机号等
    :param kwargs: others
    :return: 返回的相当于是我们处理好的json响应
    """
    json_dict = {
        "error_number": error_number,
        "error_message": error_message,
        "data": data,
    }
    if kwargs and isinstance(kwargs, dict):
        # 判断**kwargs中是否有传输数据信息, 有则更新我们已有的信息
        json_dict.update(**kwargs)
    return JsonResponse(json_dict, json_dumps_params={'ensure_ascii': False})
