from django.conf.urls import url
from . import views 

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^UserAuthBack/',views.UserAuthBack,name='UserAuthBack'),
]