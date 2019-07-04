from django.shortcuts import render,redirect
from datetime import datetime
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    """主页"""
    # if not request.session.get('user_wxopenid', None):
    #     request.session['current_url'] = request.get_full_path()
    #     return redirect('')  # 去跳转微信鉴权地址 
    return render(request, 'GameEnter/index.html', {
        'title':'主页',
        'year': datetime.now().year
    })

    

def UserAuthBack(request):
    """微信授权回调"""
    appid = ''  #微信分配
    secret = ''  #微信后台分配
    to_url = request.session.get('current_url', '/game')  # 鉴权后要跳转的地址
    # print(request.path)
    print(request.get_full_path())
    if request.method == 'GET':
        # 获取用户信息流程
        # 第一步：通过返回的code获取（网页鉴权的）access_token（时效两个小时）和openID  其中返回的refresh_token（时效三十天） 可以刷新access_token 
        # 第二步：获取全局的access_token，并存入数据库作为全局变量
        # 第三步：获取用户基本信息，（包括是不是关注用户），如果不是关注用户则需要第四步来获取详细信息
        # 第三步：如果是显示鉴权，而且不是关注用户 则 通过返回的access_token和openID获取用户详细信息，但是鉴权机制需要是 snsapi_userinfo
        code = request.GET.get('code', None)
        state = request.GET.get('state', None)
        if not code:
            return redirect(to_url)

        # 通过 code 获取网页授权 access_token

        # 先从 session 里面获取 access_token ,看是否过期
        access_token = request.session.get('weixin_jssdk_accesstoken', None)
        openid = request.session.get('weixin_openID', None)
        is_valid = False # 有效标识
        if access_token:
            checkVaildUrl = "https://api.weixin.qq.com/sns/auth";  #验 证access_token现在是否有效。有效返回“0”
            checkVaildUrl += '?access_token='+access_token
            checkVaildUrl += '&openid='+openid
            try:
                res_check = requests.get(checkVaildUrl, timeout=3)
                if res_check.status_code == 200:
                    is_valid = res_check.json()['errcode'] # 0 表示成功
                    errmsg = res_check.json()['errmsg']
            except Exception as ex:
                print('-'*20)
                print('验证access_token有效-出错：'+ex)

        expires_in = 0  # access_token 接口调用凭证超时时间，单位 秒
        refresh_token = None  # 用户刷新 access_token

        if not access_token or is_valid != 0:
            # 如果session已经消失了或者access_token失效了，都要重新获取access_token
            getaccess_tokenUrl = "https://api.weixin.qq.com/sns/oauth2/access_token";
            getaccess_tokenUrl += '?appid=' + appid  #微 信公众号的APPID
            getaccess_tokenUrl += '&secret=' + secret  # 信公众号的secret
            getaccess_tokenUrl += '&code=' + code  # 返回的code
            getaccess_tokenUrl += '&grant_type=' + 'authorization_code' 

            try:
                res = requests.get(getaccess_tokenUrl)
            except Exception as ex:
                print('-'*20)
                print('获取access_token-出错：'+ex)

    return HttpResponse('微信鉴权回调')

