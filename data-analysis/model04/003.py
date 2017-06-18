'''
matplotlib绘图的基础

'''

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
x = np.linspace(0, 1)
print(x)

y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
print(y)

# 折线图
#plt.plot(x,y)
#plt.show()
pl.plot(x,y,'y *')
pl.show()

# 散点图
#plt.plot(x,y,'o')
#plt.show()
pl.plot(x,y,'o')
pl.show()

# 柱状图
#plt.bar(x,y)
#plt.show()
pl.bar(x,y)
pl.show()