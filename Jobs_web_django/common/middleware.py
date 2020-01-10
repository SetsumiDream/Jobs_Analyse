from django.utils.deprecation import MiddlewareMixin

from common import errors
from lib.http import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        white_list = ['/',
                      '/login/',
                      '/api/user/submit/phone/',
                      '/api/user/submit/vcode/',
                      ]

        uid = request.session.get('uid')
        if uid:
        # 如果登录了， 就把user写入request
            print(User.objects.get(id=uid))
            user = User.objects.get(id=uid)
            request.user = user
            return None
        if request.path in white_list or request.path.startswith('/api/image'):
            return None
        return render_json(code=errors.LOGIN_REQUIRED, data='请登录')