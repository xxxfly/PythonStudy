# -*- coding: utf-8

from django.conf.urls import url
from .user import views as api_user



urlpatterns =[
    url(r'^user/$', api_user.user, name='user')
]

app_name = 'api-v1'
