from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def home(request):
    """
    主页
    :param request:
    :return:
    """
    return render(request, 'lianjia/index.html', {
        'title': '主页',
        'year': datetime.now().year
    })


def about(request):
    """
    说明
    :param request:
    :return:
    """
    return render(request, 'lianjia/about.html', {
        'title': '说明',
        'year': datetime.now().year
    })



def contact(request):
    """
    说明
    :param request:
    :return:
    """
    return render(request, 'lianjia/contact.html', {
        'title': '说明',
        'year': datetime.now().year
    })


def cj_list(request, area):
    """
    成交数据
    :param request:
    :param area:
    :return:
    """
    return render(request, 'lianjia/cjlist.html', {
        'title': '成交数据',
        'year': datetime.now().year
    })


def esf_list(request, area):
    """
    二手房数据列表
    :param rquest:
    :param area:
    :return:
    """
    return render(request, 'lianjia/esflist.html', {
        'title': '二手数据',
        'year': datetime.now().year
    })

