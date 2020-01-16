"""Jobs_web_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import user.api as user_api
import job_analyse.api as job_analyse_api
import imageCDN.api as imageCDN_api

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 视图
    url(r'^', include('job_view.urls', namespace='job_view')),

    # travel
    url(r'^', include('api_travel.urls', namespace='api_travel')),

    # api  User
    url(r'^api/user/submit/phone/$', user_api.submit_phone),  # 发送短信
    url(r'^api/user/submit/vcode/$', user_api.submit_vcode),  # 发送短信

    # api  analyse
    url(r'^api/job/analyse/test/$', job_analyse_api.test),  # 画图测试

    # api  Image
    url(r'^api/image/upload/img/$', imageCDN_api.upload_img),  # 上传测试
    url(r'^api/image/load/img/$', imageCDN_api.load_img),  # 上传测试

]
