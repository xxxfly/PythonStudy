#coding:utf-8

#特点：
#每个节点有零个或多个子节点
#没有父节点的结点成为根节点
#每一个非根节点有且只有一个父节点
#除了根节点外，每个子节点可以分为多个不想交的子树



#二叉树
class Node(object):
    """树的结点"""
    def __init__(self,item):
        self.elem=item
        self.lchild=None
        self.rchild=None
    

class Tree(object):
    """二叉树"""
    def __init__(self):     
        self.root=None
    
    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            cur_node=queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild=node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild=node
                return
            else:
                queue.append(cur_node.rchild)
        
    
    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return

        queue=[self.root]

        while queue[0]:
            cur_node=queue.pop(0)
            print(cur_node.elem,end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not Node:
                queue.append(cur_node.rchild)

    def preorder_travel(self,node):
        """"先序遍历"""
        if node is None:
            return
        print(node.elem,end=" ")
        self.preorder_travel(node.lchild)
        self.preorder_travel(node.rchild)

    def midorder_travel(self,node):
        """"中序遍历"""
        if node is None:
            return        
        self.midorder_travel(node.lchild)
        print(node.elem,end=" ")
        self.midorder_travel(node.rchild)

    def lastorder_travel(self,node):
        """"后序遍历"""
        if node is None:
            return        
        self.lastorder_travel(node.lchild)        
        self.lastorder_travel(node.rchild)
        print(node.elem,end=" ")
                
        
if __name__=="__main__":
    tree=Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    tree.breadth_travel()   
    print(" ") 
    tree.preorder_travel(tree.root)
    print(" ") 
    tree.midorder_travel(tree.root)
    print(" ") 
    tree.lastorder_travel(tree.root)
    print(" ") 
