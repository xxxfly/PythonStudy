# coding:utf-8
import random


# 简单二分查找
def SampleBinarySearch(sortList,key):
    """
    简单二分查找
    @param sortList [List] 排序数组
    @param key 要查找的数据
    @return 找到数据就返回下标，否则返回None
    """
    length=len(sortList)

    # 起点下标
    start=0
    # 终点下标
    end=length-1
    while start<=end:
        # 求查找区间的中间下标值
        mid=(start+end)//2
        if sortList[mid]==key:
            return mid
        # 数组前半部分查找
        elif sortList[mid]>key:
            end=mid-1
        # 数组后半部分查找
        elif sortList[mid]<key:
            start=mid+1

    return None


def SampleBinarySearch2(orgList,start,end,key):
    """
    二分查找的递归实现
    @param orgList [list]
    @param key 要查找的数据
    @return 返回查找数据的下标
    """

    if start>end:
        return None

    mid=start+(end-start)//2
    if orgList[mid]==key:
        return mid
    elif orgList[mid]<key:
        return SampleBinarySearch2(orgList,mid+1,end,key)
    else:
        return SampleBinarySearch2(orgList,start,mid-1,key)

def BinarySearchFirstKey(orgList,key):
    """
    查找第一个值等于给定值的元素
    """
    length=len(orgList)
    low=0
    high=length-1
    while low<=high:
        mid=low+(high-low)//2
        if orgList[mid]==key:
            if mid==0 or orgList[mid-1]!=key:
                return mid
            else:
                high=mid-1
        elif orgList[mid]<key:
            low=mid+1
        else:
            high=mid-1

    return None

def BinarySearchLastKey(orgList,key):
    """
    查找最后一个值等于给定值的元素
    """
    length=len(orgList)
    low=0
    high=length-1
    while low<=high:
        mid=low+(high-low)//2
        if orgList[mid]==key:
            if mid==length-1 or orgList[mid+1]!=key:
                return mid
            else:
                low=mid+1
        elif orgList[mid]<key:
            low=mid+1
        else:
            high=mid-1
    
    return None

def BinarySearchFirstKeyOrMore(orgList,key):
    """
    查找第一个值大于或等于给定值的元素
    """
    length=len(orgList)
    low=0
    high=length-1
    while low<=high:
        mid=low+(high-low)//2
        if orgList[mid]>=key:
            if mid==0 or orgList[mid-1]<key:
                return mid
            else:
                high=mid-1
        else:
            low=mid+1
    
    return None

def BinarySearchLastKeyOrLess(orgList,key):
    """
    查找最后一个小于或等于给定值的元素
    """
    length=len(orgList)
    low=0
    high=length-1
    while low<=high:
        mid=low+(high-low)//2
        if orgList[mid]<=key:
            if mid==length-1 or orgList[mid+1]>key:
                return mid
            else:
                low=mid+1
        else:
            high=mid-1

    return None

def BinarySearchLoopSortList(orgList,key):
    """
    循环有序数组的二分查找 
    例如数组 4 5 8 9 10 11 0 2 3
    """
    length=len(orgList)
    low=0
    high=length-1
    while low<=high:
        mid=low+(high-low)//2
        if orgList[mid]==key:
            return mid
        if orgList[mid]>=orgList[0]:
            # 说明前半部分是有序的，后半部分是循环有序数组
            if key>=orgList[low] and key<orgList[mid]:
                # 说明key 在有序数组中，使用二分查找
                high=mid-1
            else:
                # 说明 key 在循环有序数组中
                low=mid+1        
        else:
            # 说明前半部分是循环有序数组，后半部分是有序的。
            if key<=orgList[high] and key>orgList[mid]:
                # 说明key 在有序数组中
                low=mid+1
            else:
                # 说明 key 在循环有序数组中
                high=mid-1
    
    return None



def main():
    l1=[random.randint(0,100) for x in range(18)]
    l1.sort()
    print('原数组：%s'%str(l1))
    l1=[4,5,8,9,10,11,0,2,3]
    print(BinarySearchLoopSortList(l1,4))
    

if __name__ == '__main__':
    main()