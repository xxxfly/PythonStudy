#coding:utf-8


# 冒泡排序算法
def bubbleSort(orgList):
    """
    冒泡排序算法
    @param orgList 数组
    """
    length=len(orgList)
    for i in range(length):
        flag=False # 提前退出冒泡排序的标识
        for j in range(0,length-i-1):
            if orgList[j]>orgList[j+1]: # 交换数据
                orgList[j],orgList[j+1]=orgList[j+1],orgList[j]
                flag=True
        if not flag: # 没有数据交换的时候，提前退出
            break


# 插入排序
def insertionSort(orgList):
    """
    插入排序算法
    @param orgList 数组
    """
    length=len(orgList)
    for i in range(1,length):
        index=i-1
        item=orgList[i]
        # 查找插入位置
        for j in range(index,-1,-1):
            if orgList[j]>item:
                index=j-1
                orgList[j+1]=orgList[j] # 数据移动
            else:
                break
        orgList[index+1]=item #插入数据


# 插入排序优化
def insertionSort2(orgList):
    """
    插入排序算法
    @param orgList 数组
    """
    length=len(orgList)
    for i in range(1,length):
        item=orgList[i]
        # 查找插入位置
        for j in range(0,i):
            if orgList[j]>item:
                # 从后往前移动数据
                for m in range(j,i): 
                    orgList[i+j-m]=orgList[i+j-m-1] #移动数据                        
                orgList[j]=item # 插入数据
                break


# 选择排序
def selectionSort(orgList):
    """
    选择排序算法，类似插入排序，但是每次会从未排序区间中找到最小的元素，将其放到已排序区间的末尾。
    @param orgList 数组
    """
    length=len(orgList)
    for i in range(length):
        minItem=orgList[i] #默认最小元素是第一个
        minIndex=i  #默认最小元素下标是第一个
        # 找出未排序区间的最小元素
        for j in range(i,length):       
            if orgList[j]<minItem:
                minItem=orgList[j]
                minIndex=j
        orgList[i],orgList[minIndex]=orgList[minIndex],orgList[i] # 交换元素


# 归并排序  
def mergeSort(list):
    """
    归并排序算法，利用分治算法，将数组一分为二为两个部分，对这两个部分分别进行排序，然后再将排好序的两部分合并在一起。
    @param list 数组
    """
    # 递归终止条件
    if len(list)<=1:
        return list
    # 找中间位置
    middle=len(list)//2
    # 分治递归
    list_pre=mergeSort(list[:middle])
    list_last=mergeSort(list[middle:])
    
    # 将数组合并
    result=[]
    result=merge(list_pre,list_last)

    return result

def merge(list_pre,list_last):
    """
    合并排序后的两个数组
    """
    # 先申请一个临时数组
    tmp=[]
    pre_point,last_point=0,0  
    while pre_point<len(list_pre) and last_point<len(list_last):
        if list_pre[pre_point]<=list_last[last_point]:
            tmp.append(list_pre[pre_point])
            pre_point+=1
        else:
            tmp.append(list_last[last_point])
            last_point+=1

    tmp+=list_pre[pre_point:]
    tmp+=list_last[last_point:]

    return tmp



depth_indx=0

# 快速排序
def quickSort(orgList,start,last):
    """
    快速排序，找出一个元素，并将列表中的其他元素，与之比较，将小于这个元素的放前面，大于这个元素的放在后面。这样讲原数组分成三个部分，左区间，分区点，右区间。直到该区间元素只有一个。
    @param list 数组
    """
    if start>=last:
        return 
    # 假设取当前数组最后一个元素为分区点
    povit=orgList[last]
    low=start 
    # 遍历数组元素，将小于分区点的元素置于左边，大于分区点的元素置于右边
    for high in range(start,last):
        if orgList[high]<povit:
            orgList[low],orgList[high]=orgList[high],orgList[low] # 交换元素
            low+=1 # 次数 low 下标代表的是 分区点应该所在的位置。

    orgList[low],orgList[last]=orgList[last],orgList[low] # 将分区点元素置于数组相应的位置。

    # 对左边的部分继续分区
    quickSort(orgList,start,low-1)
    # 对右边的部分继续分区
    quickSort(orgList,low+1,last)   

# 搜索第 k 大的元素（有问题）
def searchMax_k(orgList,start,last,k):
    """
    在一个无序数组查找第 k 大元素
    """
    if start>=last:
        return 
    
    povit=orgList[last]
    low=start
    for high in range(start,last):
        if orgList[high]<povit:
            orgList[low],orgList[high]=orgList[high],orgList[low] # 交换元素
            low+=1 # 次数 low 下标代表的是 分区点应该所在的位置。
    orgList[low],orgList[last]=orgList[last],orgList[low] # 将分区点元素置于数组相应的位置。

    print('k:%d---low:%d'%(k,low))
    if k<low+1:
        searchMax_k(orgList,start,low-1,k-low)
    elif k>low+1:
        searchMax_k(orgList,low+1,last,k-low)
    else:
        print('res:%d'%orgList[low+1])
        return orgList[low+1]


# 桶排序
def BucketSort(orgList):
    """
    桶排序，将数据分到有序的桶中，再对每个桶内的数据进行单独排序，都排序完成之后，再根据顺序依次从桶里面取出数据，组成有序序列。
    """
    pass

# 计数排序
def countSort(orgList):
    """
    计数排序,类似桶排序，只是根据数据范围，分成最大值 K 个桶
    """
    length=len(orgList)
    if length<=1:
        return orgList
    
    # 找出原数组的数据范围
    min_item=orgList[0] # 数组的最小值
    max_item=orgList[0]  # 数组的最大值
    for i in range(length):
        if min_item>=orgList[i]:
            min_item=orgList[i]
        if max_item<=orgList[i]:
            max_item=orgList[i]

    # 创建一个桶数组，桶的个数max_item-min_item+1
    bucketList=[0 for i in range(max_item-min_item+1)]
    # 将原数组每个元素的个数置于 桶 数组相应的位置
    for i in range(length):
        bucketList[orgList[i]-min_item]+=1
    
    # 对桶数组的元素顺序求和
    for i in range(1,len(bucketList)):
        bucketList[i]+=bucketList[i-1]
    
    # 创建排序数组，其大小跟原数组一样
    sortList=[None for i in range(length)]
    # 倒序遍历原数组，将其元素赋值到排序数组中
    for i in range(length-1,-1,-1):
        current_index=bucketList[orgList[i]-min_item]
        sortList[current_index-1]=orgList[i]
        bucketList[orgList[i]-min_item]-=1
    
    # 将排序后的数组元素赋值给原数组
    for i in range(length):
        orgList[i]=sortList[i]
    
# 基数排序
def RadixSort(orgList):
     """
     基数排序,对排序数据进行高低位划分，先根据倒数第一位开始排序，借助稳定排序算法（桶排序或者计数排序），然后根据倒数第二位进行排序，最后到第一位。
     """   
     pass

# 荷兰国旗问题
def HollandFlagProblem(orgList):
    """
    荷兰国旗问题，荷兰国旗有三个颜色，依次是 红 白 蓝，现在有一数组里面有很多这样的三种颜色，如何有序排列成荷兰国旗
    假设红 白 蓝 分别代表数字  0、1、2
    """
    length=len(orgList)
    if length<=1:
        return orgList
    start=0 # 假设 sart 为红色，在数组前面部分
    current=0 # 假设curent 为 白色，在数组中间部分
    end=length-1 # 假设end 为 蓝色，在数组结尾部分
    while current<=end:
        if orgList[current]==0:
            orgList[start],orgList[current]=orgList[current],orgList[start]
            start+=1    
            current+=1
        elif orgList[current]==1:
            current+=1
        elif orgList[current]==2:
            orgList[end],orgList[current]=orgList[current],orgList[end]
            end-=1
    

def main():
    l1=[4,3,5,3,9,1,2,1]
    # countSort(l1)
    # print(l1)
    l2=[1,2,0,1,1,0,2,2,0]
    HollandFlagProblem(l2)
    print(l2)

if __name__ == '__main__':
    main()