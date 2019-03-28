# coding:utf-8


class DoubleNode(object):
    """双向节点"""
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return not self.__head

    def length(self):
        """链表长度"""
        # count用来记录数量
        count = 0
        # cur游标，用来移动遍历结点
        currentNode = self.__head
        while currentNode != None:
            count += 1
            currentNode = currentNode.next
        return count

    def travel(self):
        """遍历整个链表"""
        # cur游标，用来移动遍历结点
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        """在链表头部添加结点"""
        node = DoubleNode(item)
        # if self.__head==None:
        #     self.__head=node
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            node.next.prev = node
            self.__head = node

    def append(self, item):
        """在链表末尾添加结点"""
        node = DoubleNode(item)
        # if self.__head==None:
        #     self.__head=node
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """在指定位置添加结点"""
        node = DoubleNode(item)
        if pos<=0:
            self.add(item)
        # 如果 pos 的位置 超过原链表的最大长度，则默认直接在链表最后面添加结点
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.__head
            # 定义当前的下标  初始为0
            curIndex = 0
            # 定义当前节点的前一个结点，初始为None
            preNode = None
            while cur != None:
                # 在当前位置插入新的结点
                if curIndex == pos:
                    # if preNode != None:
                    #     preNode.next = node
                    #     node.prev=preNode
                    # else:
                    #     # 如果前结点为空，则认为在第一个位置插入新的结点
                    #     self.__head = node
                    # node.next = cur
                    # cur.prev=node
                    node.next=cur
                    node.prev=cur.prev
                    cur.prev=node
                    node.prev.next=node
                    break
                preNode = cur
                cur = cur.next
                curIndex += 1

    def remove(self, item):
        """删除结点"""
        cur = self.__head
        # 定义当前节点的前一个结点，初始为None
        preNode = None
        while cur != None:
            # 如果能够匹配这个结点的值，则删除
            if cur.elem == item:
                # if preNode != None:
                #     # 让前一个结点直接指向下一个结点
                #     preNode.next = cur.next
                # else:
                #     self.__head = cur.next
                if cur==self.__head:
                    self.__head=cur.next
                    if cur.next:
                        #判断链表是否只有一个结点
                        cur.next.prev=None
                else:
                    cur.prev.next=cur.next
                    if cur.next:
                        cur.next.prev=cur.prev
                break
            preNode = cur
            cur = cur.next

    def search(self, item):
        """查找结点是否存在"""
        searchFlag = False
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                searchFlag = True
                print('找到了')
                break
            cur = cur.next
        if not searchFlag:
            print('没有找到')


if __name__ == "__main__":
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(10)
    print(dll.is_empty())
    print(dll.length())

    print("")
    print('---从链表末尾插入新的结点---')
    dll.append(30)
    dll.append(20)
    dll.append(152)
    dll.travel()

    print("")
    print('---从链表头插入新的结点---')
    dll.add(65)
    dll.travel()

    print("")
    print('---从链表特定位置插入新的结点---')
    dll.insert(0,123)
    dll.insert(3,36)
    dll.travel()

    print("")
    print('---移除某个结点---')
    dll.remove(152)
    dll.travel()
