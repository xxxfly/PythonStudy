#-*- coding:utf-8 -*-


#自定义数组类
class myArray():
    def __init__(self,n):
        #初始化一个固定长度的数组，只是数组元素都为 None
        self.arr=[None for i in range(n)] 
        self.count=0
        self.len=n

    def insert(self,val):
        if self.count==len(self.arr):
            sum=0
            for i in self.arr:
                sum+=i
            self.arr[0]=sum
            self.count=1
        self.arr[self.count]=val
        self.count+=1
    
    def add(self,val):
        if self.count>=len(self.arr):
            #数组空间不够了
            #重新申请了一个 2 倍大小的空间数组
            new_arr=[None for i in range(2*len(self.arr))]
            #把原来数组中的元素一次 copy 带 new_arr中
            j=0
            while j<len(self.arr):
                new_arr[j]=self.arr[j]
                j+=1
            #将 new_arr 复制给 arr,此时 arr 就是 原来的两倍大小了
            self.arr=new_arr
        
        #将 值 val 添加到 相应的下标下面
        self.arr[self.count]=val
        self.count+=1
            

    def show(self):
        for i in self.arr:
            print(str(i)+' ',end='')
        print('')

def main():
    myArr=myArray(3)
    # # for i in range(4):
    # #     myArr.insert(i+1)
    # #     myArr.show()
    
    for i in range(14):
        myArr.add(i+1)
        myArr.show()

if __name__ == '__main__':
    main()