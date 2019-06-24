# -*- coding: utf-8

from django.conf.urls import url
from .user import views as api_user
from .lianjia import views as api_lianjia

urlpatterns = [
    url(r'^user/$', api_user.user, name='user'),
    url(r'^lianjia/$', api_lianjia.cjlist, name='cjlist')
]

app_name = 'api-v1'
