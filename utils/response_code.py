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
    # SMSERROR = "4006"
    # SMSFAIL = "4007"
    #
    USERNAMEEXIST = "2"
    USERNAMELENGTH = "6"
    USERNAMEFORMAT = "7"
    USERNAMEEMPTY = "5"
    USEREMAILEMPTY = "8"
    USEREMAILERROR = "3"
    USERTELEPHONEERROR = "4"
    # SESSIONERR = "4101"
    # LOGINERR = "4102"
    # PARAMERR = "4103"
    # USERERR = "4104"
    # ROLEERR = "4105"
    # PWDERR = "4106"
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
    # ResponseCode.SMSERROR: "发送短信验证码异常",
    # ResponseCode.SMSFAIL: "发送短信验证码失败",
    #
    ResponseCode.USERNAMEEMPTY: "用户名为空",
    ResponseCode.USERNAMELENGTH: "用户名长度过长或过短",
    ResponseCode.USERNAMEFORMAT: "用户名格式错误",
    ResponseCode.USERNAMEEXIST: "用户名已存在",
    ResponseCode.USEREMAILEMPTY: "邮箱为空",
    ResponseCode.USEREMAILERROR: "邮箱格式错误",
    ResponseCode.USERTELEPHONEERROR: "手机号码格式错误",
    # ResponseCode.SESSIONERR: "用户未登录",
    # ResponseCode.LOGINERR: "用户登录失败",
    # ResponseCode.PARAMERR: "参数错误",
    # ResponseCode.USERERR: "用户不存在或未激活",
    # ResponseCode.ROLEERR: "用户身份错误",
    # ResponseCode.PWDERR: "密码错误",
    #
    # ResponseCode.SERVERERR: "内部错误",
    # ResponseCode.UNKOWNERR: "未知错误",
}
