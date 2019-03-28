#-*- coding:utf-8 -*-


# 顺序栈
class ArrayStack():
    """用数组实现的顺序栈"""
    def __init__(self,length):
        """
        初始化顺序栈长度
        @param length
        """
        self.__stack=[None for i in range(length)]
        self.__len=length
        self.__count=0
    
    def isEmpty(self):
        """验证栈是否为空"""
        # return not self.__stack
        return []==self.__stack

    def push(self,item):
        """从栈顶添加一个元素"""
        # 时间复杂度和空间复杂度都是 O(1)

        # 如果栈内元素已满，则添加失败
        if self.__len == self.__count:
            return False
        self.__stack[self.__count]=item
        self.__count+=1
        return True

    def pop(self):
        '''从栈顶取出一个元素'''
        # 时间复杂度和空间复杂度都是 O(1)

        #栈为空，则直接返回 None
        if self.isEmpty():
            return None    
        item=self.__stack[self.__count-1] 
        self.__count-=1
        return item

#链表结点
class LinkNode():
    """链表结点"""
    def __init__(self,value):
        self.elm=value
        self.next=None


# 链式栈
class LinkStack():
    """基于链表实现的栈"""
    def __init__(self,node=None):
        self.head=node

    def is_empty(self):
        """判断栈是否为空"""
        return not self.head

    def push(self,value):
        """入栈操作"""
        node=LinkNode(value)
        # 验证栈是否为空
        if self.is_empty():
            self.head=node
            return True
        # 定义临时结点为当前结点
        currentNode=self.head
        # 遍历栈，找到最后一个结点
        while currentNode.next!=None:
            currentNode=currentNode.next
        currentNode.next=node
        return True

    def pop(self):
        """出栈操作"""
        if self.is_empty():
            return None
        # 定义临时结点为当前结点
        currentNode=self.head
        # 定义当前节点的前一个结点
        preNode=None
        while currentNode.next!=None:
            preNode=currentNode
            currentNode=currentNode.next
        preNode.next=None
        return currentNode.elm


def test1():
    st=ArrayStack(5)

    st.push(1)
    st.push(2)
    st.push(3)

    print(st.pop())
    print(st.pop())

    st.push('a')
    st.push('b')
    print(st.pop())

def test2():
    st=LinkStack()

    st.push(1)
    st.push(2)
    st.push(3)

    print(st.pop())
    print(st.pop())

    st.push('a')
    st.push('b')
    print(st.pop())


def main():
    # test1()
    test2()

if __name__ == '__main__':
    main()

