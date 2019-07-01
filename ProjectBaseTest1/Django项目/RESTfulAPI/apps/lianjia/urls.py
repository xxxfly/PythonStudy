
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contract'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^cjlist/(?P<area>\w+)/$', views.cj_list, name='cj-list'),
    url(r'^esflist/(?P<area>\w+)/$', views.esf_list, name='esf-list'),
]
