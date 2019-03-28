#-*- coding:utf-8 -*-

# 顺序队列
class ArrayQueue(object):
    """用数组实现的队列（固定长度）"""
    def __init__(self,length):
        """
        初始化队列
        @param length[int] 数组的长度
        """
        self.__queue=[None for i in range(length)]
        self.__len=length # 队列长度
        self.__head=0 # 队列头下标
        self.__tail=0 # 队列尾下标
    
    def is_empty(self):
        """判断队列是否为空"""
        return self.__head==self.__tail

    def enqueue(self,value):
        """
        入队操作
        @param value
        """
        #队列已满
        if self.__len == self.__tail:
            return False
        # 在队列尾部添加一个元素
        self.__queue[self.__tail]=value
        self.__tail+=1

    def dequeue(self):
        """出队操作"""
        # 队列为空格
        if self.__tail==self.__head:
            return None
        item=self.__queue[self.__head]
        self.__head+=1

        return item


# 顺序队列
class ArrayQueue2(object):
    """用数组实现的队列（优化）"""
    def __init__(self,length):
        """
        初始化队列
        @param length[int] 数组的长度
        """
        self.__queue=[None for i in range(length)]
        self.__len=length # 队列长度
        self.__head=0 # 队列头下标
        self.__tail=0 # 队列尾下标
    
    def is_empty(self):
        """判断队列是否为空"""
        return self.__head==self.__tail

    def enqueue(self,value):
        """
        入队操作
        @param value
        """
        #队列已满
        if self.__len == self.__tail:
            if self.__head==0:
                return False
            for i in range(self.__head,self.__tail):
                self.__queue[i-self.__head]=self.__queue[i]
            self.__tail-=self.__head
            self.__head=0
        # 在队列尾部添加一个元素
        self.__queue[self.__tail]=value
        self.__tail+=1
        return True

    def dequeue(self):
        """出队操作"""
        # 队列为空格
        if self.__tail==self.__head:
            return None
        item=self.__queue[self.__head]
        self.__head+=1

        return item

class LinkNode(object):
    """链表结点"""
    def __init__(self,value):
        self.elm=value
        self.next=None

class LinkQueue(object):
    """基于链表的队列结构"""
    def __init__(self,node=None):
        self.__head=node
    
    def is_empty(self):
        """判断队列是否为空"""
        return not self.__head

    def enqueue(self,value):
        """入队操作"""
        node=LinkNode(value)
        if self.is_empty():
            self.__head=node
            return True
        
        # 在链表的结尾插入新的结点
        currentNode=self.__head
        while currentNode.next!=None:
            currentNode=currentNode.next
        currentNode.next=node
        return True

    def dequeue(self):
        """出队操作"""
        if self.is_empty():
            return None
        item=self.__head.elm
        self.__head=self.__head.next
        return item

#循环队列
class LoopQueue(object):
    """"循环队列"""
    def __init__(self,length):
        self.__queue=[None for i in range(length)]
        self.__len=length
        self.__head=0
        self.__tail=0

    def is_Empty(self):
        """判断队列是否为空"""
        return self.__head==self.__tail

    def enqueue(self,value):
        """
        入队操作
        @param value 元素
        """
        # 队列已满的情况(当前tail 指向的位置数据空缺)
        if (self.__tail+1)%self.__len==self.__head:
            return False
        self.__queue[self.__tail]=value
        # self.__tail+=1
        # if self.__tail>=self.__len:
        #     self.__tail=0
        self.__tail=(self.__tail+1)%self.__len
        return True

    def dequeue(self):
        """出队操作"""
        if self.is_Empty():
            return None
        item=self.__queue[self.__head]
        # self.__head+=1
        # if self.__head>=self.__len:
        #     self.__head=0
        self.__head=(self.__head+1)%self.__len
        return item



def test1():
    que=ArrayQueue(5)
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)

    print(que.dequeue())
    print(que.dequeue())

    que.enqueue('a')
    que.enqueue('b')
    print(que.dequeue())
    print(que.dequeue())
    print(que.enqueue('c'))

def test2():
    que=ArrayQueue2(5)
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)

    print(que.dequeue())
    print(que.dequeue())

    que.enqueue('a')
    que.enqueue('b')
    print(que.dequeue())
    print(que.dequeue())
    que.enqueue('c')
    print(que.dequeue())
    print(que.dequeue())

def test3():
    lq=LoopQueue(5)
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    print(lq.enqueue(5))
    print(lq.dequeue())
    print(lq.dequeue())
    lq.enqueue('a')
    lq.enqueue('b')
    lq.enqueue('c')
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())


def main():
    test3()

if __name__ == '__main__':
    main()