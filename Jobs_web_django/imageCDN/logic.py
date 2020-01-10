import os

from django.conf import settings

from lib.qiniu import upload_img
from Jobs_web_django import config
from worker import call_by_worker
from imageCDN.models import ImageUrl


@call_by_worker
def handle_upload(img, target, class_target):
    filename = '%s_%s' % (target, class_target)
    file_path = os.path.join(settings.BASE_DIR, settings.MEDIAS, filename)
    # 写入模式不能追加模式
    with open(file_path, mode='wb') as fp:
        for chunk in img.chunks():
            fp.write(chunk)

    # 上传到七牛云
    upload_img(filename, file_path)
    image, _ = ImageUrl.objects.get_or_create(name=filename)
    image.url, image.target, image.class_target = (config.QN_URL + filename), target, class_target
    image.save()
    os.remove(file_path)