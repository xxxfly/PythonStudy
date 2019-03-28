#-*-conding:utf-8-*-
import redis


# try:
#     r=redis.StrictRedis(host='127.0.0.1',port=6379,password='123456')
# except Exception as ex:
#     print(ex)

#操作方式1，直接操作读写
# r.set('name','zx-1')
# print(r.get('name'))

# print(r.keys('*'))


#操作方式2，pipeline
# pipe=r.pipeline()
# pipe.hset('h-py','name','h-test')
# pipe.hset('h-py','gender',1)
# pipe.execute()


# print(r.hget('h-py','name'))
# print(r.hget('h-py','gender'))


#封装
class redisHelper(object):
    def __init__(self,host,port,password):
        self.__redis=redis.StrictRedis(host=host,port=port,password=password)
    def set(self,key,value):
        self.__redis.set(key,value)
    def get(self,key):
        return self.__redis.get(key)

        
def main():
    pass

if __name__ == '__main__':
    main()



