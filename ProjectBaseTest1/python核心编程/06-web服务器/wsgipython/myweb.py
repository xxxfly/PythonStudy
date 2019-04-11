# coding:utf-8
import time


class Application(object):
    """
    框架的核心部分，也就是框架的主题程序，框架是通用的
    """
    def __init__(self,urls):
        self.urls=urls
    
    def __call__(self,env,start_response):
        path=env.get('PATH_INFO','/')
        if path.startwith('/static'):
            # 要访问静态文件
            file_name=path[7:]
            # 打开文件，读取内容
        for url,handler in self.urls:
            # ("/m_time",show_time)
            if path==url:
                return handler(env,start_response)
        
        # 没有找到
        status="404 Not Found"
        headers=[]
        start_response(status,headers)
        return "not found"
            

def show_time(env,start_response):
    headers=[
        ('Content-Type','text/plain')
    ]
    status_code="200 OK"
    start_response(status,headers)
    return time.ctime()

def say_hello(env,start_response):
    headers=[
        ('Content-Type','text/plain')
    ]
    status_code="200 OK"
    start_response(status,headers)
    return "hello world"

app=Application()


