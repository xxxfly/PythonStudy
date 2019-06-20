from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """
    主页
    :param request:
    :return:
    """
    return HttpResponse('<h1>主页</h1>')

def about(request):
    """
    说明
    :param request:
    :return:
    """
    return HttpResponse('<h1>说明</h1>')


def cj_list(request, area):
    """
    成交数据
    :param request:
    :param area:
    :return:
    """
    return HttpResponse('<h1>成交列表</h1>'+area)


def esf_list(rquest, area):
    """
    二手房数据列表
    :param rquest:
    :param area:
    :return:
    """
    return HttpResponse('<h1>二手房列表</h1>'+area)

