#encoding:utf-8

def mergeSort(orgList):
    """递归排序"""
    n=len(orgList)
    if n<=1:
        return orgList
    middle=n//2
    #left_li 采用归并排序后形成新的有序列表
    left_li=mergeSort(orgList[:middle])
    #right_li 采用归并排序后形成新的有序列表
    right_li=mergeSort(orgList[middle:])

    #将两个有序的子序列合并成一个整体
    # merage(left_li,right_li)
    left_pointer,right_pointer=0,0
    result=[]
    while left_pointer<len(left_li) and right_pointer<len(right_li):
        if left_li[left_pointer]<right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer+=1
        else:
            result.append(right_li[right_pointer])
            right_pointer+=1

    result+=left_li[left_pointer:]
    result+=right_li[right_pointer:]
    return result

if __name__=="__main__":
    a = [33, 2, 34, 123, 56, 47, 87, 38, 26, 88, 52, 9, 17, 28, 243]
    print(a)
    sortA=mergeSort(a)
    print(a)
    print(sortA)