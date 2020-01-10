from qiniu import Auth, put_file, etag

from Jobs_web_django import config
from common import keys


def upload_img(filename, file_path):

    q = Auth(config.QN_AK, config.QN_SK)
    bucket_name = 'setsumi0v0'
    token = q.upload_token(bucket_name, filename, 3600)
    ret, info = put_file(token, filename, file_path)
    print(ret)
    print(info)