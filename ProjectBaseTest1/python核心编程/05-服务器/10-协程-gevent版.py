#-*-coding:utf-8-*-

from gevent import monkey
import gevent
from urllib import request

# def test(n):
#     for i in range(n):
#         print('%s,%d'%(gevent.getcurrent(),i))
#         gevent.sleep(0.5)

# g1=gevent.spawn(test,5)
# g2=gevent.spawn(test,5)
# g3=gevent.spawn(test,5)

# g1.join()
# g2.join()
# g3.join()

#有IO才做时需要这一句
monkey.patch_all()

def myDownload(url):
    print('GET:%s'%url)
    resp=request.urlopen(url)
    data=resp.read()
    print('%d bytes received from %s'%(len(data),url))

gevent.joinall([
    gevent.spawn(myDownload,'http://www.baidu.com/'),
    gevent.spawn(myDownload,'http://www.itcast.cn/'),
    gevent.spawn(myDownload,'http://www.itheima.com/')
])