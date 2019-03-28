# coding:utf-8


class TreeLinkNode():
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None

# 前序遍历
def pre_order(root):
    if root:
        yield root.val
        yield from pre_order(root.left)
        yield from pre_order(root.right)    
# 中序遍历
def in_order(root):
    if root:
        yield from in_order(root.left)
        yield root.val
        yield from in_order(root.right)
# 后序遍历
def post_order(root):
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.val




if __name__=="__main__":
    nodeA=TreeLinkNode('A')
    nodeB=TreeLinkNode('B')
    nodeC=TreeLinkNode('C')
    nodeD=TreeLinkNode('D')
    nodeE=TreeLinkNode('E')
    nodeF=TreeLinkNode('F')
    nodeG=TreeLinkNode('G')
    nodeH=TreeLinkNode('H')
    nodeI=TreeLinkNode('I')
    nodeJ=TreeLinkNode('J')

    nodeA.left,nodeA.right=nodeB,nodeC
    nodeB.left,nodeB.right=nodeD,nodeE
    nodeC.left,nodeC.right=nodeF,nodeG
    nodeD.left,nodeD.right=nodeH,nodeI
    nodeE.left=nodeJ

    print(list(pre_order(nodeA)))



