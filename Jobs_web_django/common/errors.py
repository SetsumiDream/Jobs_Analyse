SMS_ERROR = 1000
VCODE_ERROR = 1001
LOGIN_REQUIRED = 1002


class LogicError(Exception):
    code = 0
    data = ''

    def __str__(self):
        return self.__class__.__name__


def gen_logic_error(name, code, data):
    return type(name, (LogicError,), {'code': code, 'data': data})


SmsError = gen_logic_error('SmsError', code=1000, data='发送短信失败')
VcodEerror = gen_logic_error('VcodEerror', code=1001, data='验证码错误')
LoginRequired = gen_logic_error('LoginRequired', code=1002, data='请登录')