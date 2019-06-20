
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^cjlist/(?P<area>\w+)/$', views.cj_list, name='cj-list'),
    url(r'^esflist/(?P<area>\w+)/$', views.esf_list, name='esf-list'),
]
