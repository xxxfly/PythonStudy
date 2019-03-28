# coding:utf-8

class SingleCycleNode(object):
    """单链表的结点"""
    def __init__(self,elem):
        """结点元素"""
        self.elem=elem
        """结点的指向"""
        self.next=None

#node=SingleCycleNode(100)

class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self,node=None):
        self.__head=node
        if node:
            node.next=node
    def is_empty(self):
        """链表是否为空"""
        return not self.__head
    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        #count用来记录数量
        count=1        
        #cur游标，用来移动遍历结点
        currentNode=self.__head
        while currentNode.next!=self.__head:
            count+=1
            currentNode=currentNode.next            
        return count
                                                
    def travel(self):
        """遍历整个链表"""
        #cur游标，用来移动遍历结点
        cur=self.__head
        while cur!=None:
            print(cur.elem,end=" ")
            if cur.next==self.__head:
                break
            cur=cur.next
            
    def add(self,item):
        """在链表头部添加结点"""
        node=SingleCycleNode(item)
        # if self.__head==None:
        #     self.__head=node
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            cur=self.__head            
            node.next=cur                      
            while cur!=None:
                if cur.next==self.__head:
                    cur.next=node
                    break
                cur=cur.next                
            self.__head=node
    def append(self,item):
        """在链表末尾添加结点"""
        node=SingleCycleNode(item)
        # if self.__head==None:
        #     self.__head=node
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            cur=self.__head
            while cur!=None:
                if cur.next==self.__head:
                    break
                cur=cur.next
            node.next=cur.next
            cur.next=node
            
    def insert(self,pos,item):
        """在指定位置添加结点"""
        node=SingleCycleNode(item)
        #如果 pos 的位置 超过原链表的最大长度，则默认直接在链表最后面添加结点
        if pos<=0:
            self.add(item)            
        elif pos>=self.length(): 
            self.append(item)
        else:         
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
                #验证是否是最后一个
                if cur.next==self.__head:
                    #找到最后一个结点，就退出
                    break
                preNode=cur
                cur=cur.next
                curIndex+=1
                
    def remove(self,item):
        """删除结点"""
        if self.is_empty():
            return
        cur=self.__head
        #定义当前节点的前一个结点，初始为None
        preNode=None 
        while cur!=None:
            #如果能够匹配这个结点的值，则删除
            if cur.elem==item:
                #判读是不是头结点
                if cur==self.__head:
                    #头结点的情况
                    #找到尾结点
                    rear=self.__head
                    #如果链表只有一个结点
                    if rear.next==self.__head:
                        self.__head=None                                         
                    else: 
                        #链表多个结点 
                        while rear.next!=self.__head:
                            rear=rear.next                                                                 
                        self.__head=cur.next
                        rear.next=self.__head
                else:
                    #让前一个结点直接指向下一个结点
                    preNode.next=cur.next
                break
            if cur.next==self.__head:
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
            if cur.next==self.__head:
                break
            cur=cur.next            
        if not searchFlag:
            print('没有找到')
    
if __name__=="__main__":
    pass
    scll=SingleCycleLinkList()
    print(scll.is_empty())
    print(scll.length())

    print("")
    print('---从链表末尾插入新的结点---')
    scll.append(10)
    print(scll.is_empty())
    print(scll.length())
    scll.travel()

    print("")
    print('---从链表末尾插入新的结点---')
    scll.append(30)
    scll.append(20)
    scll.append(152)
    scll.travel()

    print("")
    print('---从链表头插入新的结点---')
    scll.add(65)
    scll.travel()

    print("")
    print('---从链表特定位置插入新的结点---')
    scll.insert(0,123)
    scll.insert(3,36)
    scll.travel()

    print("")
    print('---移除某个结点---')
    scll.remove(152)
    scll.remove(10)
    scll.remove(123)
    scll.travel()

