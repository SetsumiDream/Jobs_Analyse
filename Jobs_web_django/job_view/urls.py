from django.conf.urls import url


from . import views
urlpatterns = [
    url(r'^$', views.rd_view, name='rd_view'),
    url(r'^login/$', views.login, name='login'),
    url(r'^main/$', views.main, name='main'),
    url(r'^jobs_analyse/$', views.jobs_analyse, name='jobs_analyse'),
]