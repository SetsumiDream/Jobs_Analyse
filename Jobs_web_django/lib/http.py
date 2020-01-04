"""封装JSON数据"""
import json

from django.conf import settings
from django.http import HttpResponse


def render_json(code=0, data=None):
    dic = {
        'code': code,
        'data': data
    }
    if settings.DEBUG:
        dic_dumps = json.dumps(dic, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        dic_dumps = json.dumps(dic, ensure_ascii=False, separators=[',', ':'])
    return HttpResponse(dic_dumps)
