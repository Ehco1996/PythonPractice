#通过Python 计算一元二次方程
#二次方程的基本格式 ax**2 + bx + c = 0

import cmath

print("二次方程的基本格式 ax^2 + bx + c = 0")
a = float(input('输入a：'))
b = float(input("输入b："))
c = float(input("输入c："))

dlet = (b**2) - (4*a*c)

#注意这里引入了复数的概念，通过cmath计算得到答案
anw1 = (-b-cmath.sqrt(dlet))/(2*a)
anw2 = (-b+cmath.sqrt(dlet))/(2*a) 
print("结果为{} 和 {}".format(anw1,anw2))
