#conding：utf-8


def insertSort(orgList):
    """插入排序"""
    # #从右边的无序序列中取出多少个元素执行这样的过程
    # for i in range(1,len(orgList)):
    #     j=i-1 #代表内层循环的起始值
    #     curI=i
    #     while j>=0: #与前面的有序数组的元素，从后往前匹配大小            
    #         if orgList[j]>orgList[curI]:
    #             orgList[j],orgList[curI]=orgList[curI],orgList[j]
    #             curI=j
    #             j=j-1
    #         else:
    #             break

    #从右边的无序序列中取出多少个元素执行这样的过程
    for i in range(1,len(orgList)):
        j=i #代表内层循环的起始值
        while j>0: #与前面的有序数组的元素，从后往前匹配大小            
            if orgList[j]<orgList[j-1]:
                orgList[j],orgList[j-1]=orgList[j-1],orgList[j]
                j=j-1
            else:
                break
            
if __name__=="__main__":
    a=[33,21,2,4,123,234,43,68,36]
    print(a)
    insertSort(a)
    print(a)