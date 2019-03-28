#coding:utf-8

def bubbleSort(orgList):
    """冒泡排序"""
    n=len(orgList)
    for i in range(n-1):
        count=0
        #每一轮循环 都是判断前一个数与后一个数的大小，并把较大的数移到后面去
        for j in range(n-1-i):
            if orgList[j]>orgList[j+1]:
                orgList[j],orgList[j+1]=orgList[j+1],orgList[j]
        if count==0:
            return
    for val in orgList:
        print(val)

if __name__=='__main__':
    a=[22,1,223,43,23,567,334,38,34]
    bubbleSort(a)