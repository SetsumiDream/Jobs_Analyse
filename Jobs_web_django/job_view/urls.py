from django.conf.urls import url


from . import views
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^main/$', views.main, name='main')
]