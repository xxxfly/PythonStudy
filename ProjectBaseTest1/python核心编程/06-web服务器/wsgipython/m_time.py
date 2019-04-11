import time

def say_time():
    return time.ctime()

def fun1():
    pass

def application(env,handle_headers):
    # env={
    #     "PATH_INFO":'',
    #     "QUERY_STRING":''
    # }
    headers=[
        ('Content-Type','text/plain')
    ]
    status_code="200 OK"
    handle_headers(status_code,headers)
    return time.ctime()