'''
更详细的定制matplotlib画出来的图
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

plt.plot(x,y,'r--')
plt.title('this is title')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper')
plt.show()ç