# -*- coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 一维数据集
def OneDimensionalData():
    np.random.seed(1000)
    y=np.random.standard_normal(20) # 20 个随机数 数组
    x=range(len(y))
    # plt.plot(x,y)
    plt.plot(y.cumsum(),'b') # 基础的绘图函数，接收 x y 数组值
    plt.grid(True)
    plt.axis('tight') # 
    plt.set_cmap('hot')
    plt.xlim(-1,20)  # 设置x 轴最小值和最大值
    plt.ylim(np.min(y.cumsum())-1,np.max(y.cumsum())+1) # 设置y 轴最小值和最大值
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('A Sample Plot')
    plt.show()

# 二维数据集
def DoubleDimensionalData():
    np.random.seed(2000)
    y=np.random.standard_normal((20,2)).cumsum(axis=0) # 二维数组
    plt.figure(figsize=(7,4))
    # plt.plot(y,lw=1.5)
    plt.plot(y[:,0],lw=1.5,label='1st') # 第一组数据
    plt.plot(y[:,1],lw=1.5,label='2nd') # 第二组数据
    plt.plot(y,'ro')
    plt.grid(True)
    plt.legend(loc=0)  # 图例   loc 图例位置
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('A Simple Plot')
    plt.show()

# 两个Y轴
def DoubleDimensionalData2():
    np.random.seed(2000)
    y=np.random.standard_normal((20,2)).cumsum(axis=0)
    y[:,0]=y[:,0]*100
    fig,ax1=plt.subplots()
    plt.figure(figsize=(7,4))
    plt.plot(y[:,0],'b',lw=1.5,label='1st')
    plt.plot(y[:,0],'ro')
    plt.grid(True)
    plt.legend(loc=8)  # 图例   loc 图例位置
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value 1st')
    plt.title('A Simple Plot')
    
    ax2=ax1.twinx()
    plt.plot(y[:,1],'g',lw=1.5,label='2nd')
    plt.plot(y[:,1],'ro')
    plt.legend(loc=0)
    plt.ylabel('value 2nd')
    plt.show()

# 两个坐标轴，上下
def DoubleDimensionalData3():
    np.random.seed(2000)
    y=np.random.standard_normal((20,2)).cumsum(axis=0)
    y[:,0]=y[:,0]*100

    plt.figure(figsize=(7,5))

    plt.subplot(211)
    plt.plot(y[:,0],lw=1.5,label='1st')
    plt.plot(y[:,0],'ro')
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.ylabel('value')
    plt.title('A Simple Plot')

    plt.subplot(212)
    plt.plot(y[:,1],'g',lw=1.5,label='2nd')
    plt.plot(y[:,1],'ro')
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')

    plt.show()

# 两个坐标轴 左右
def DoubleDimensionalData4():
    np.random.seed(2000)
    y=np.random.standard_normal((20,2)).cumsum(axis=0)

    plt.figure(figsize=(9,4))

    plt.subplot(121)
    plt.plot(y[:,0],lw=1.5,label='1st')
    plt.plot(y[:,0],'ro')
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('1st Data Set')

    plt.subplot(122)
    plt.bar(np.arange(len(y)),y[:,1],width=0.5,color='g',label='2nd')
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.xlabel('index')
    plt.title('2nd Data Set')

    plt.show()

# 散点图
def ScatterPlot1():
    np.random.seed(2000)
    y=np.random.standard_normal((1000,2))

    # 构建坐标系
    plt.figure(figsize=(7,5))
    plt.plot(y[:,0],y[:,1],'ro')
    plt.grid(True)
    plt.xlabel('1st')
    plt.ylabel('2nd')
    plt.title('Scatter Plot')

    plt.show()

# 散点图
def ScatterPlot2():
    np.random.seed(2000)
    y=np.random.standard_normal((1000,2))
    
    plt.figure(figsize=(7,5))
    plt.scatter(y[:,0],y[:,1],marker='o')
    plt.grid(True)
    plt.xlabel('1st')
    plt.ylabel('2nd')
    plt.title('Scatter Plot')

    plt.show()

# 散点图 第三维
def ScatterPlot3():
    np.random.seed(2000)
    y=np.random.standard_normal((1000,2))
    c=np.random.randint(0,10,len(y))

    plt.figure(figsize=(7,5))
    plt.scatter(y[:,0],y[:,1],c=c,marker='o')
    plt.colorbar()
    plt.grid(True)
    plt.xlabel('1st')
    plt.ylabel('2nd')
    plt.title('Scatter Plot')

    plt.show()


# 直方图
def Histogram1():
    np.random.seed(2000)
    y=np.random.standard_normal((500,2))
    
    plt.figure(figsize=(7,4))
    plt.hist(y,label=['1st','2nd'],bins=15)
    plt.grid(True)
    plt.legend(loc=0)
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.title('Histogram')

    plt.show()


# 箱形图
def BoxPlot():
    np.random.seed(2000)
    y=np.random.standard_normal((1000,2))

    fig,ax=plt.subplots(figsize=(7,4))
    plt.boxplot(y)
    plt.grid(True)
    plt.setp(ax,xticklabels=['1st','2nd'])
    plt.xlabel('data set')
    plt.ylabel('value')
    plt.title('Boxplot')

    plt.show()


if __name__ == "__main__":
    # OneDimensionalData()
    # DoubleDimensionalData()
    # DoubleDimensionalData2()
    # DoubleDimensionalData3()
    # DoubleDimensionalData4()
    # ScatterPlot1()
    # ScatterPlot2()
    # ScatterPlot3()
    # Histogram1()
    BoxPlot()