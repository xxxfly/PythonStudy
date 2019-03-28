# coding:utf-8

class SingleNode(object):
    """单链表的结点"""
    def __init__(self,elem):
        """结点元素"""
        self.elem=elem
        """结点的指向"""
        self.next=None

#node=SingleNode(100)

class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=None):
        self.__head=node
    def is_empty(self):
        """链表是否为空"""
        return not self.__head
    def length(self):
        """链表长度"""
        #count用来记录数量
        count=0        
        #cur游标，用来移动遍历结点
        currentNode=self.__head
        while currentNode!=None:
            count+=1
            currentNode=currentNode.next            
        return count
                                                
    def travel(self):
        """遍历整个链表"""
        #cur游标，用来移动遍历结点
        cur=self.__head
        while cur!=None:
            print(cur.elem,end=" ")
            cur=cur.next
    def add(self,item):
        """在链表头部添加结点"""
        node=SingleNode(item)
        # if self.__head==None:
        #     self.__head=node
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            node.next=cur
            self.__head=node        
    def append(self,item):
        """在链表末尾添加结点"""
        node=SingleNode(item)
        # if self.__head==None:
        #     self.__head=node
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def insert(self,pos,item):
        """在指定位置添加结点"""
        node=SingleNode(item)
        #如果 pos 的位置 超过原链表的最大长度，则默认直接在链表最后面添加结点
        if pos>=self.length(): 
            self.append(item)
        else:
            if pos<0:
                pos=0
            cur=self.__head
            #定义当前的下标  初始为0
            curIndex=0 
            #定义当前节点的前一个结点，初始为None
            preNode=None 
            while cur!=None:
                #在当前位置插入新的结点
                if curIndex==pos:  
                    if preNode!=None:
                        preNode.next=node
                    else:
                        #如果前结点为空，则认为在第一个位置插入新的结点
                        self.__head=node 
                    node.next=cur
                    break
                preNode=cur
                cur=cur.next
                curIndex+=1
                
    def remove(self,item):
        """删除结点"""
        cur=self.__head
        #定义当前节点的前一个结点，初始为None
        preNode=None 
        while cur!=None:
            #如果能够匹配这个结点的值，则删除
            if cur.elem==item:
                if preNode!=None:
                    #让前一个结点直接指向下一个结点
                    preNode.next=cur.next
                else:                    
                    self.__head=cur.next
                break
            preNode=cur
            cur=cur.next
    def search(self,item):
        """查找结点是否存在"""
        searchFlag=False
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                searchFlag=True
                print('找到了')
                break
            cur=cur.next
        if not searchFlag:
            print('没有找到')
    
if __name__=="__main__":
    sll=SingleLinkList()
    print(sll.is_empty())
    print(sll.length())

    sll.append(10)
    print(sll.is_empty())
    print(sll.length())

    print("")
    print('---从链表末尾插入新的结点---')
    sll.append(30)
    sll.append(20)
    sll.append(152)
    sll.travel()

    print("")
    print('---从链表头插入新的结点---')
    sll.add(65)
    sll.travel()

    print("")
    print('---从链表特定位置插入新的结点---')
    sll.insert(0,123)
    sll.insert(3,36)
    sll.travel()

    print("")
    print('---移除某个结点---')
    sll.remove(152)
    sll.travel()

