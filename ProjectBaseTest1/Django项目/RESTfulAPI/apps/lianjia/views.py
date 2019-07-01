from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import timezone
from datetime import datetime
import pytz
from apps.user.models import User
from .forms import UserForm,RegisterForm
import random
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
    print(request.session.get('is_login',False))
    if request.session.get('is_login',False):
        return redirect('/lianjia/')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user=User.objects.get(user_name=username)    
                if user.mobile == password:
                    request.session['is_login'] = True
                    request.session['user_guid'] = user.id
                    request.session['user_name'] = user.user_name
                    return redirect('/lianjia/')
                else:
                    message = '账户或密码不正确！'
  
            except User.DoesNotExist:
                message = '登录失败！'

        return render(request,'lianjia/login.html',{
            'title': '登录',
            'year': datetime.now().year,
            'message':message,
            # 'login_form':login_form
        })
    login_form = UserForm() # Django form 表单
    return render(request, 'lianjia/login.html', {
        'title': '登录',
        'year': datetime.now().year,
        'message':'',
        # 'login_form':login_form  # 暂时不采用这种
    })

def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.session.get('is_login',False):
        redirect('/lianjia/')
    if request.method == 'POST':
        message = '请检查填写的内容！'

        # 通过表单验证提交的数据是否合规
        # registerForm = RegisterForm(request.POST)
        # if registerForm.is_valid():
        #     pass
        username = request.POST.get('username','')
        nickname = request.POST.get('nickname','')
        password = request.POST.get('password','')
        mobile = password
        guid = 'u'+datetime.now().strftime('%Y%m%d%H%M%S')+str(random.randrange(1000,9999))

        try:  
            print('-'*10)                      
            new_user=User()
            new_user.user_guid=guid
            new_user.user_name=username
            new_user.real_name=nickname
            new_user.mobile=mobile
            new_user.balance=100
            new_user.all_balance=80
            new_user.available_balance=50
            new_user.create_date=datetime.now(pytz.utc)
            new_user.last_login_date=datetime.now(pytz.utc)
            new_user.gender=1
            new_user.province='河南'
            new_user.save()

            request.session['is_login'] = True
            request.session['user_guid'] = new_user.user_guid
            request.session['user_name'] = new_user.user_name
            return redirect('/lianjia/')

        except Exception as ex:
            message='注册失败！'
        
        return render(request,'lianjia/login.html',{
            'title': '注册',
            'year': datetime.now().year,
            'message':message,
        })
            
        
    return render(request, 'lianjia/register.html', {
        'title': '注册',
        'year': datetime.now().year,
    })

def logout(request):
    """注销"""
    request.session.flush()
    return redirect('lianjia')

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

