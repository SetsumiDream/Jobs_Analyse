from django.conf.urls import url


from . import views
urlpatterns = [
    url(r'^api/travel/test/$', views.test, name='test'),
    url(r'^api/travel/near_to_far/$', views.near_to_far),
    url(r'^api/travel/cheap_to_expensive/$', views.cheap_to_expensive),
    url(r'^api/travel/expensive_to_cheap/$', views.expensive_to_cheap),
    url(r'^api/travel/common_more_to_less/$', views.common_more_to_less),
    url(r'^api/travel/detail/$', views.detail),
    url(r'^api/travel/smart_sort/$', views.smart_sort),
]