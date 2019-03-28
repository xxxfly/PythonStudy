# -*- coding=utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

# 将两个一维数组转化为二维数组
strike=np.linspace(50,150,24)
ttm=np.linspace(0.5,2.5,24)
strike,ttm=np.meshgrid(strike,ttm)

# 根据新的 ndarray 对象，通过简单的比例调整二次函数生成模拟的隐含波动率
iv=(strike-100)**2/(100*strike)/ttm

fig=plt.figure(figsize=(9,6))
ax=fig.gca(projection='3d')

surf=ax.plot_surface(strike,ttm,iv,rstride=2,cstride=2,cmap=plt.cm.coolwarm,linewidth=0.5,antialiased=True)

ax.set_xlabel('strike')
ax.set_ylabel('tim-to-maturity')
ax.set_zlabel('implied volatility')

fig.colorbar(surf,shrink=0.5,aspect=5)

plt.show()