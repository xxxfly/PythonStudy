# coding:utf-8

class Dequeue(object):
    """双端队列"""
    def __init__(self):
        self.__list=[]
    def add_front(self,item):
        """从头部添加元素"""
        self.__list.insert(0,item)
    def add_rear(self,item):
        """在尾部添加元素"""
        self.__list.append(item)
    def pop_front(self):
        """从队列头部取出元素"""
        return self.__list.pop(0)
    def pop_rear(self):
        """从队列尾部取出元素"""
        return self.__list.pop()
    def is_empty(self):
        """判断双端队列是否为空"""
        return not self.__list
    def size(self):
        """获取双端队列的长度"""
        return len(self.__list)

if __name__=="__main__":
    d=Dequeue()
    d.add_front(1)
    d.add_front(2)
    d.add_front(3)
    d.add_front(4)
    d.add_rear(4)
    d.add_rear(5)
    d.add_rear(6)
    d.add_rear(7)
    print(d.pop_front())
    print(d.pop_front())
    print(d.pop_rear())
    print(d.pop_rear())