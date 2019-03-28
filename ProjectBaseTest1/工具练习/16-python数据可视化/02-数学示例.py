# -*- coding:utf-8 -*-
import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

# 求积分的函数
def func(x):
    return 0.5*np.exp(x)+1

# 定义积分区间
a,b=0.5,1.5
x=np.linspace(0,2)
y=func(x)

# 绘制函数图形
fig,ax=plt.subplots(figsize=(7,5))
plt.plot(x,y,'b',linewidth=2)
plt.ylim(ymin=0)

# 使用 Polygon 函数生成阴影部分，表示积分面积
Ix=np.linspace(a,b)
Iy=func(Ix)
verts=[(a,0)]+list(zip(Ix,Iy))+[(b,0)]
poly=Polygon(verts,facecolor='0.7',edgecolor='0.5')
ax.add_patch(poly)

# plt.txt 和 plt.figtext 在图表上添加数学公式和一些坐标轴标签。 LaTeX 代码在两个美元符号之前传递($...$)。两个函数的前面两个参数都是放置对应文本的坐标值
plt.text(0.5*(a+b),1,r"$\int_a^b fx\mathrm{d}x$",horizontalalignment='center',fontsize=20)
plt.figtext(0.9,0.075,'$x$')
plt.figtext(0.075,0.9,'$f(x)$')

# 设置 x 和 y 刻度标签的位置
ax.set_xticks((a,b))
ax.set_xticklabels(('$a$','$b$'))
ax.set_yticks([func(a),func(b)])
ax.set_yticklabels(('$f(a)$','$f(b)$'))
plt.grid(True)

plt.show()

if __name__ == "__main__":
    pass