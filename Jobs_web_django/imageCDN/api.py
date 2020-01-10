import random

from django.shortcuts import render

from imageCDN.logic import handle_upload
from imageCDN.models import ImageUrl
from lib.http import render_json


def upload_img(request):
    """
    :param request: img图片数据 target用途 class_target分类标志
    示例： background_1
    :return:
    """
    img = request.FILES.get('img')
    target = request.POST.get('target')
    class_target = request.POST.get('class_target')
    # 分块写入本地
    user = request.user
    print(user.id)
    if user.id == 1:
        handle_upload(img, target, class_target)
        return render_json()
    return render_json(code=1, data='权限不足')


def load_img(request):
    target = request.GET.get('target')
    img = ImageUrl.objects.filter(target=target)
    url = random.choice(img).url
    return render_json(data=url)