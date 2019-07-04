from django.shortcuts import render,redirect
from datetime import datetime
from django.http import HttpResponse
import requests
import logging

# Create your views here.
def index(request):
    """主页"""
    # if not request.session.get('user_wxopenid', None):
    #     request.session['current_url'] = request.get_full_path()
    #     return redirect('')  # 去跳转微信鉴权地址 
    logger = logging.getLogger('log')  # 日志对象 
    logger.info('主页请求地址：' + request.get_full_path())
    return render(request, 'GameEnter/index.html', {
        'title':'主页',
        'year': datetime.now().year
    })

    

def UserAuthBack(request):
    """微信授权回调"""
    appid = ''  #微信分配
    secret = ''  #微信后台分配

    logger = logging.getLogger('log')  # 日志对象 
    logger.info('用户鉴权回调地址：'+request.get_full_path())
    to_url = request.session.get('current_url', '/game')  # 鉴权后要跳转的地址
    logger.info('鉴权后要跳转的地址：'+to_url)
    
    
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
            logger.info('网页授权access_token验证有效地址：'+checkVaildUrl)
            try:
                res_check = requests.get(checkVaildUrl, timeout=3)
                logger.info('网页授权access_token验证有效结果：'+res_check.text)
                if res_check.status_code == 200:
                    is_valid = res_check.json()['errcode'] # 0 表示成功
                    errmsg = res_check.json()['errmsg']
            except Exception as ex:
                logger.error('网页授权access_token验证有效出错' + str(ex))

        expires_in = 0  # access_token 接口调用凭证超时时间，单位 秒
        refresh_token = None  # 用户刷新 access_token
        scope = None    # 用户授权的作用域，使用逗号（,）分隔
        if not access_token or is_valid != 0:
            # 如果session已经消失了或者access_token失效了，都要重新获取access_token
            getaccess_tokenUrl = "https://api.weixin.qq.com/sns/oauth2/access_token";
            getaccess_tokenUrl += '?appid=' + appid  #微 信公众号的APPID
            getaccess_tokenUrl += '&secret=' + secret  # 信公众号的secret
            getaccess_tokenUrl += '&code=' + code  # 返回的code
            getaccess_tokenUrl += '&grant_type=' + 'authorization_code' 
            logger.info('通过code换取网页授权access_token地址：' + getaccess_tokenUrl)
            try:
                res = requests.get(getaccess_tokenUrl)
                logger.info('通过code换取网页授权access_token结果：' + res.text)
                if res.status_code == 200:
                    res_json = res.json()
                    access_token = res_json['access_token']
                    expires_in = res_json['expires_in']
                    refresh_token = res_json['refresh_token']
                    openid = res_json['openid']
                    scope = res_json['scope']

                    # 将信息保存至session
                    request.session['weixin_jssdk_accesstoken'] = access_token
                    request.session['weixin_openID'] = access_token
            except Exception as ex:
                logger.error('通过code换取网页授权access_token出错：' + str(ex))

        
        # 获取全局 access_token
        # 先去数据库 验证当前全局 access_token 是否已经过期
        base_access_token = None
        base_expires_in = 0
        if not base_access_token:
            # 去获取全局 access_token ,次数有限制
            get_base_access_tokenUrl = "https://api.weixin.qq.com/cgi-bin/token"
            get_base_access_tokenUrl += '?grant_type='+'client_credential'
            get_base_access_tokenUrl += '&appid='+ appid
            get_base_access_tokenUrl += '&secret='+secret
            logger.info('获取全局access_token地址：'  + get_base_access_tokenUrl)
            try:
                res_base = requests.get(get_base_access_tokenUrl)
                logger.info('获取全局access_token结果：' + res_base.text)
                if res_base.status_code == 200:
                    res_base_json = res_base.json()
                    base_access_token = res_base_json['access_token'] # 默认时效两小时
                    base_expires_in = res_base_json['expires_in']

                    # 保存至数据库
                    
            except Exception as ex:
                logger.error('获取全局access_token错误：' + str(ex))
            

        # 获取用户基本信息 日限量五百万次
        base_subscribe = None
        base_openid = None
        base_nickname = None
        base_sex = None
        base_language = None
        base_city = None
        base_province = None
        base_country = None
        base_headimgurl = None
        base_subscribe_time = None
        base_unionid = None
        base_remark = None
        base_groupid = None
        base_tagid_list = None

        try:
            get_base_userinfoUrl = "https://api.weixin.qq.com/cgi-bin/user/info"
            get_base_userinfoUrl += '?access_token=' + base_access_token
            get_base_userinfoUrl += '&openid=' + openid
            get_base_userinfoUrl += '&lang=' + 'zh_CN'
            logger.info('获取用户基本信息地址：' + get_base_userinfoUrl)
            res_base_user = requests.get(get_base_userinfoUrl)
            logger.info('获取用户基本信息地址结果：' + res_base_user.text)
            if res_base_user.status_code == 200:
                res_base_user_json = res_base_user.json()

                base_subscribe = res_base_user_json['subscribe']  # 关注状态 0未关注 1关注
                if base_subscribe == 1:
                    base_openid = res_base_user_json['openid']
                    base_nickname = res_base_user_json['nickname']
                    base_sex = res_base_user_json['sex']
                    base_language = res_base_user_json['language']
                    base_city = res_base_user_json['city']
                    base_province = res_base_user_json['province']
                    base_country = res_base_user_json['country']
                    base_headimgurl = res_base_user_json['headimgurl']
                    base_subscribe_time = res_base_user_json['subscribe_time']
                    base_remark = res_base_user_json['remark']
                    base_groupid = res_base_user_json['groupid']

                    # 保存session
                    request.session['weixin_user_nickname'] = base_nickname
                    request.session['weixin_user_sex'] = base_sex
                    request.session['weixin_user_province'] = base_province
                    request.session['weixin_user_city'] = base_city
                    request.session['weixin_user_country'] = base_country
                    request.session['weixin_user_unionid'] = base_unionid
                    request.session['weixin_user_subscribe_time'] = base_subscribe_time
                    request.session['weixin_user_remark'] = base_remark
                    request.session['weixin_user_headimgurl'] = base_headimgurl
        except Exception as ex:
            logger.error('获取用户基本信息错误：' + str(ex))


        # 显示授权
        if state == 'snsapi_userinfo' and base_subscribe != 1:
            # 拉取用户信息(需scope为 snsapi_userinfo)
            get_user_url = "https://api.weixin.qq.com/sns/userinfo"

            get_user_url += '?access_token=' + access_token
            get_user_url += '&openid=' + openid
            get_user_url += '&lang=' + 'zh_CN'
            logger.info('拉取用户信息结果地址：' + get_user_url)
            try:
                res_user = requests.get(get_user_url)
                logger.info('拉取用户信息结果：' + res_user.text)
                if res_user.status_code == 200:
                    res_user_json = res_user.json()
                    user_openid = res_user_json['openid']
                    User_nickname = res_user_json['nickname']
                    user_sex = res_user_json['sex']
                    user_province = res_user_json['province']
                    user_city = res_user_json['city']
                    user_country = res_user_json['country']
                    user_headimgurl = res_user_json['headimgurl']

                    request.session['weixin_user_nickname'] = User_nickname
                    request.session['weixin_user_sex'] = user_sex
                    request.session['weixin_user_province'] = user_province
                    request.session['weixin_user_city'] = user_city
                    request.session['weixin_user_country'] = user_country
                    request.session['weixin_user_headimgurl'] = user_headimgurl
            except Exception as ex:
                logger.error('拉取用户信息结果出错：' + str(ex))
            
        # 跳转至相应页面
        # 包括处理失败的页面，默认页面，鉴权前的页面
        return redirect(to_url)
            




    return HttpResponse('微信鉴权回调')

