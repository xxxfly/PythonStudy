from django.conf.urls import  url
from . import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^about/$',views.about,name='about'),
    url(r'^add-user/(?P<id>\d+)/$',views.add,name='add-user'),
]