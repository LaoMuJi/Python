from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index),
    # url(r'^showarg(\d+)$', views.show_arg),
    url(r'^showarg(?P<num>\d+)$', views.show_arg), # 捕获url参数
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^test_ajax$', views.ajax_test),
    url(r'^ajax_handle$', views.ajax_handle),
    url(r'^login_ajax$', views.login_ajax),
    url(r'^login_ajax_check$', views.login_ajax_check),
]
