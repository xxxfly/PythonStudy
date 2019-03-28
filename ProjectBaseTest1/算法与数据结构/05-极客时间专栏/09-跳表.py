# coding=utf-8
"""
    跳表是一种实现方法
    跳表中存储的是正整数，并且储存的是不重复的
"""

from typing import Optional
import random

class LinkNode(object):
    def __init__(self,data:Optional[int]=None):
        self._data=data
        self._forwords=[] # Forward pointers

# 跳表
class SkipList(object):

    _MAX_LEVEL=16

    def __init__(self):
        self._level_count=1
        self._head=LinkNode()
        self._head._forwords=[None] * type(self)._MAX_LEVEL
    
    def insert(self,value:int):
        level=self._random_level()
        if self._level_count<level:self._level_count=level
        new_node=LinkNode(value)
        new_node._forwords=[None]*level
        update=[self._head]*level   # update is like a list of prevs

        p=self._head
        for i in range(level-1,-1,-1):
            while p._forwords[i] and p._forwords[i]._data<value:
                p=p._forwords[i]
            update[i]=p  # Found a prev
        for i in range(level):
            new_node._forwords[i]=update[i]._forwords[i] # new_node.next=prev.next
            update[i]._forwords[i]=new_node #prev.next=new_node
            
    def find(self,value:int)->Optional[LinkNode]:
        p=self._head
        for i in range(self._level_count-1,-1,-1): # Move down a level
            while p._forwords[i] and p._forwords[i]._data<value:
                p=p._forwords[i] # Move along level
        return p._forwords[0] if p._forwords[0] and p._forwords[0]._data==value else None
    
    def delete(self,value):
        update=[None]*self._level_count
        p=self._head
        for i in range(self._level_count-1,-1,-1):
            while p._forwords[i] and p._forwords[i]._data < value:
                p=p._forwords[i]
            update[i]=p
        
        if p._forwords[0] and p._forwords[0]._data==value:
            for i in range(self._level_count-1,-1,-1):
                if update[i]._forwords[i] and update[i]._forwords[i]._data==value:
                    update[i]._forwords[i]=update[i]._forwords[i]._forwords[i] #Sililar to prev.next = prev.next.next
    
    def _random_level(self,p:float=0.5)->int:
        level=1        
        while random.random()<p and level<type(self)._MAX_LEVEL:
            level+=1
        # print("_random_level:%d"%level)
        return level

    def __repr__(self)->str:
        values=[]
        p=self._head
        while p._forwords[0]:
            values.append(str(p._forwords[0]._data))
            p=p._forwords[0]
        return "->".join(values)
    
if __name__ == "__main__":
    sl=SkipList()
    for i in range(100):
        sl.insert(i)
    print(sl)
    p=sl.find(58)
    print(p._data)
