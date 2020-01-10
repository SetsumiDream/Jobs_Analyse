from django.core.cache import cache

from lib.sms import send_sms
from common import errors
from lib.http import render_json
from common import keys
from user.models import User


def submit_phone(request):
    """提交手机发送验证码"""
    phone = request.POST.get('phone')
    # 发送验证码
    send_sms(phone)

    return render_json()


def submit_vcode(request):
    """提交短信验证码"""
    phone = request.POST.get('phone')
    vcode = request.POST.get('vcode')
    cached_vcode = cache.get(keys.VCODE_KEY % phone)
    if vcode == cached_vcode and vcode is not None:
        user, _ = User.objects.get_or_create(phonenum=phone, defaults={'nickname': phone})
        request.session['uid'] = user.id
        return render_json(data=user.to_dict())
    else:
        return render_json(code=errors.VCODE_ERROR, data='验证码错误')
