import logging

from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from common import errors
from common.errors import LogicError
from lib.http import render_json
from user.models import User


logger = logging.getLogger('err')


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        white_list = ['/',
                      '/login/',
                      '/api/user/submit/phone/',
                      '/api/user/submit/vcode/',
                      '/favicon.ico',
                      '/api/travel',
                      ]

        uid = request.session.get('uid')
        print(request.path)
        if uid:
        # 如果登录了， 就把user写入request
            print(User.objects.get(id=uid))
            user = User.objects.get(id=uid)
            request.user = user
            return None
        if request.path in white_list or request.path.startswith('/api/image') or request.path.startswith('/api/travel'):
            return None
        return redirect('job_view:login')


class LogicErrorMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):

        if isinstance(exception, LogicError):
            logger.error('LogicError: {0}'.format(exception))
            return render_json(code=exception.code, data=exception.data)