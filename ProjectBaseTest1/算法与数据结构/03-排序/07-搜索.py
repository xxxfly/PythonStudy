#coding:utf-8

#二分查找
def binary_search(orgList,item):
    """二分查找"""
    n=len(orgList)
    if n>0:        
        midder=n//2
        if orgList[midder]==item:
            return True
        elif orgList[midder]>item:
            return binary_search(orgList[0:midder],item)
        else:
            return binary_search(orgList[midder+1:],item)
    return False    

def binary_search2(orgList,item):
    """二分查找,非递归"""
    n=len(orgList)
    first=0
    last=n-1
    while first<=last:
        mid=(first+last)//2
        if orgList[mid]==item:
            return True
        elif item<orgList[mid]:
            last=mid-1
        else:
            first=mid+1
    return False


if __name__=="__main__":
    li=[3,6,23,31,45,47,55,123,132,143]
    print(binary_search(li,45))
    print(binary_search(li,49))

    print(binary_search2(li,45))
    print(binary_search2(li,49))