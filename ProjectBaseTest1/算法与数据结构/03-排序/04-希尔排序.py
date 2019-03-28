#coding:utf-8

def shellSort(orgList):
    """希尔排序"""
    n=len(orgList)
    gap=n//2
    #gap变化到0之前，插入算法执行的次数
    while gap>0:
        #插入算法，与普通的插入算法的区别就是gap的步长
        for j in range(gap,n):
            #j=[gap,gap+1,gap+2,...,n-1]
            i=j
            while i>0:
                if orgList[i]<orgList[i-gap]:
                    orgList[i],orgList[i-gap]=orgList[i-gap],orgList[i]
                    i-=gap
                else:
                    break
        #缩短gap步长
        gap//=2

    

if __name__=="__main__":
    a=[33,2,34,123,56,47,87,38,26,88,52,9,17,28,243]
    print(a)
    shellSort(a)
    print(a)