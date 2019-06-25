from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from apps.user.models import User
from .forms import UserForm
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

def login(request):
    """
    登录
    :param request:
    :return:
    """
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user=User.objects.get(user_name=username)
                if user.mobile == password:
                    return redirect('/lianjia/')
                else:
                    message = '账户或密码不正确！'
            except:
                message = '账户或密码不正确！'
        return render(request,'lianjia/login.html',{
            'title': '登录',
            'year': datetime.now().year,
            'message':message,
            'login_form':login_form
        })
    login_form = UserForm()
    return render(request, 'lianjia/login.html', {
        'title': '登录',
        'year': datetime.now().year,
        'message':'',
        'login_form':login_form
    })

def register(request):
    """
    注册
    :param request:
    :return:
    """
    return render(request, 'lianjia/register.html', {
        'title': '注册',
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

