#-*-conding:utf-8-*-
import redis

#封装
class RedisHelper(object):
    '''Redis帮助类'''
    def __init__(self,host,port,password):
        self.__redis=redis.StrictRedis(host=host,port=port,password=password)
    def set(self,key,value):
        self.__redis.set(key,value)
    def get(self,key):
        return self.__redis.get(key)