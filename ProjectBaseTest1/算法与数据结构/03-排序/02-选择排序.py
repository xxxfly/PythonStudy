#coding:utf-8


def selectSort(orgList):
    """选择排序"""
    # for i in range(0,len(orgList)):
    #     for j in range(i+1,len(orgList)):
    #         if orgList[i]>orgList[j]:
    #             orgList[i],orgList[j]=orgList[j],orgList[i]
    n=len(orgList)
    for j in range(0,n-1): # j:0~n-2
        min_index=j
        for i in range(j+1,n):
            if orgList[min_index]>orgList[i]:
                min_index=i
        orgList[j],orgList[min_index]=orgList[min_index],orgList[j]


if __name__=='__main__':
    a=[22,1,223,43,23,567,334,38,34]
    print(a)
    selectSort(a)
    print(a)