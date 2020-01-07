import random

import requests
from django.core.cache import cache

from worker import call_by_worker
from Jobs_web_django import config
from common import keys


def gen_vcode(size=4):
    start = 10 ** (size - 1)
    end = 10 ** size - 1
    return str(random.randint(start, end))


@call_by_worker
def send_sms(phone):
    params = config.YZX_PARAMS.copy()
    params['mobile'] = phone
    vcode = gen_vcode()
    cache.set(keys.VCODE_KEY % phone, vcode, timeout=180)
    params['param'] = vcode
    print(vcode)
    resp = requests.post(config.YZX_URL, json=params)
    if resp.status_code == 200:
        result = resp.json()
        if result['code'] == '000000':
            return True, 'OK'
        else:
            print(result['code'])
            return False, result['msg']
    else:
        return False, '访问短信服务器有误'
