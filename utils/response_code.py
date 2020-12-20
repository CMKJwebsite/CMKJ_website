# Create your response code here.
class ResponseCode:
    """
    错误代码,在引发错误的时候作为错误的标志
    """
    OK = "0"
    NOPRODUCTDATA = "1"
    # DBERROR = "4001"
    # NODATA = "4002"
    # DATAEXIST = "4003"
    # DATAERR = "4004"
    # METHERR = "4005"
    #
    USERNAMEEXIST = "2"
    USERNAMELENGTH = "6"
    USERNAMEFORMAT = "7"
    USERNAMEEMPTY = "5"
    USEREMAILEMPTY = "8"
    USEREMAILERROR = "3"
    USERTELEPHONEEMPTY = "9"
    USERTELEPHONELENGTH = "10"
    USERTELEPHONEERROR = "4"
    USERTELEPHONEEXIST = "11"
    USERPASSWORDEMPTY = "12"
    USERPASSWORDLENGTH = "13"
    USERPASSWORDERROR = "14"
    USERREPASSWORDEMPTY = "15"
    USERREPASSWORDERROR = "16"
    USERVERIFICATIONCODEEMPTY = "17"
    USERVERIFICATIONCODEERROR = "18"
    # SESSIONERR = "4101"
    # LOGINERR = "4102"
    # PARAMERR = "4103"
    # USERERR = "4104"
    # ROLEERR = "4105"
    #
    # SERVERERR = "4500"
    # UNKOWNERR = "4501"


error_map = {
    # 错误信息,与错误代码对应
    ResponseCode.OK: "成功",
    ResponseCode.NOPRODUCTDATA: "无产品数据",
    # ResponseCode.DBERROR: "数据库查询错误",
    # ResponseCode.DATAEXIST: "数据已存在",
    # ResponseCode.DATAERR: "数据错误",
    # ResponseCode.METHERR: "方法错误",

    ResponseCode.USERNAMEEMPTY: "用户名为空",
    ResponseCode.USERNAMELENGTH: "用户名长度过长或过短",
    ResponseCode.USERNAMEFORMAT: "用户名格式错误",
    ResponseCode.USERNAMEEXIST: "用户名已存在",
    ResponseCode.USEREMAILEMPTY: "邮箱为空",
    ResponseCode.USEREMAILERROR: "邮箱格式错误",
    ResponseCode.USERTELEPHONEEMPTY: "手机号码为空",
    ResponseCode.USERTELEPHONELENGTH: "手机号码长度过长或过短",
    ResponseCode.USERTELEPHONEERROR: "手机号码格式错误",
    ResponseCode.USERTELEPHONEEXIST: "手机号码已存在",
    ResponseCode.USERPASSWORDEMPTY: "密码为空",
    ResponseCode.USERPASSWORDLENGTH: "密码长度过长或过短",
    ResponseCode.USERPASSWORDERROR: "密码强度过低",
    ResponseCode.USERREPASSWORDEMPTY: "确认密码为空",
    ResponseCode.USERREPASSWORDERROR: "确认密码与密码不一致",
    ResponseCode.USERVERIFICATIONCODEEMPTY: "验证码为空",
    ResponseCode.USERVERIFICATIONCODEERROR: "验证码错误",
    # ResponseCode.SESSIONERR: "用户未登录",
    # ResponseCode.LOGINERR: "用户登录失败",
    # ResponseCode.PARAMERR: "参数错误",
    # ResponseCode.USERERR: "用户不存在或未激活",
    # ResponseCode.ROLEERR: "用户身份错误",
    #
    # ResponseCode.SERVERERR: "内部错误",
    # ResponseCode.UNKOWNERR: "未知错误",
}
