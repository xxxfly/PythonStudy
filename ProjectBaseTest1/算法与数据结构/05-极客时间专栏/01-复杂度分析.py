#-*- coding:utf-8 -*-



#假设每行代码的执行时间都一样，为 unit_time
#第2、3行代码都执行了一遍，各自需要1个 unit_time，第4、5、6代码都运行了 n 遍，所以需要 3n*unit_time
#这段代码总的执行时间就为 (3n+2)*unit_time。
#复杂度 O(n)
def cal1(n):
    sum=0
    i=1
    while i<=n:
        sum+=i
        i+=1
    return sum

#复杂度O(n平方)
def cal2(n):
    sum=0
    i=1
    while i<=n:
        j=1
        while j<=n:
            sum=sum+i*j
            j+=1
        i+=1
    return sum

#复杂度O(logn)
def cal3(n):
    i=0
    while i<=n:
        i=i*2   

def cal4(n):
    list=[]
    i=0
    while i<=n:
        list.append(i*i)
        i+=1
    for item in list:
        print(item)

#假设 list 的长度为 n
def cal5(list,x):
    pos=-1
    i=0
    while i < len(list):
        if list[i]==x:
            pos=i
        i+=1
    return pos

#假设 list 的长度为 n
def cal6(list,x):
    pos=-1
    i=0
    while i < len(list):
        if list[i]==x:
            pos=i
            break
        i+=1
    return pos



def main():
    print(cal1(5))
    print(cal2(5))
  

if __name__ == '__main__':
    main()