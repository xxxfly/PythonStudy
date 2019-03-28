#-*- coding:utf-8 -*-


class SingleLinkNode(object):
    """单链表的结点"""
    def __init__(self,value):
        self.elem=value
        self.next=None

#自定义单链表
class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=None):
        #初始化链表头指向的结点
        self.__head=node

    def is_empty(self):
        """判断单链表是否为空"""
        return not self.__head
    def length(self):
        """单链表长度"""
        #count用来记录数量
        count=0;
        #currentNode代表当前节点
        currentNode=self.__head
        while currentNode!=None:
            count+=1
            currentNode=currentNode.next
        return count

    def travle(self):
        """遍历单链表"""
        currentNode=self.__head
        while currentNode!=None:
            print(currentNode.elem,end=" ")
            currentNode=currentNode.next
        
    def add(self,value):
        """在单链表头部添加元素"""
        #构建新元素的结点
        node=SingleLinkNode(value)
        currentNode=self.__head        
        node.next=currentNode
        self.__head=node
    
    def append(self,value):
        """在单链表的末尾添加元素"""
        node=SingleLinkNode(value)
        if self.is_empty():
            self.__head=node
        else:
            currentNode=self.__head
            while currentNode.next!=None:
                currentNode=currentNode.next
            currentNode.next=node
    
    def reverse(self):
        """链表反转"""
        if self.is_empty():
            return
        currentNode=self.__head
        preNode=None
        while currentNode.next!=None:   
            nextNode=currentNode.next         
            currentNode.next=preNode
            preNode=currentNode
            currentNode=nextNode
        currentNode.next=preNode
        self.__head=currentNode
    
    def checkRing(self):
        """链表中环的检测"""
        pass

    def removeDescNode(self,n):
        """删除链表倒数第 n 个结点"""
        # n 必须大于 0
        if n<1:
            return
        # 空链表不操作
        if self.is_empty():
            return    
        length=self.length()
        # 当 n 的长度大于链表的长度时，直接删除第一个结点
        if n>=length:
            self.__head=self.__head.next
            return
        # 当前节点
        currentNode=self.__head
        # 前驱结点
        preNode=None
        # 当前下标
        index=0 
        while index!=length-n:
            preNode=currentNode
            currentNode=currentNode.next
            index+=1
        print('currentNode:%d'%currentNode.elem)
        preNode.next=currentNode.next


    def getMiddleNode(self):
        """获取链表的中间结点"""
        if self.is_empty():
            return None
        length=self.length()
        middleIndex=int(length/2)
        curIndex=0
        currentNode=self.__head
        while curIndex!=middleIndex:
            currentNode=currentNode.next
            curIndex+=1
            
        return currentNode

    def getHead(self):
        return self.__head

def checkHuiWen(nodeList):
    """验证回文"""
    pass
    if nodeList.is_empty():
        return False
    length=nodeList.len()
    if length==1:
        return True
    if length==2:
        if nodeList.getHead()==nodeList.getHead().next:
            return True
        else:
            return False
        
    currentNode=nodeList.getHead()
    slowIndex=currentNode
    fastIndex=currentNode.next.next
    while currentNode.next!=None:
        slowIndex


def main():
    sl=SingleLinkList()
    sl.append(1)
    sl.append(2)
    sl.append(3)
    sl.append(4)
    sl.append(5)
    sl.travle()
    print('')
    # sl.reverse()
    # sl.travle()
    # print('')
    sl.removeDescNode(2)
    sl.travle()
    print('')

if __name__ == '__main__':
    main()