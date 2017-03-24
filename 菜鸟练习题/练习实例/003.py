#计算用户输入的数字的平方根

#version 1 只能计算正数的平方根，不能计算负数和复数的平方根
num = float(input("请输入一个数字：  "))
num_sqrt = num **0.5
print("{:.3f} 的平方根是 {:.3f}".format(num,num_sqrt))

#version2 引入模块cmath 解决上述问题
import cmath
num1  = int(input("请输入一个数字 ："))
num1_sqrt =cmath.sqrt(num1)
print("{}的平方根为{:0.3f}+{:0.3f}j".format(num1,num1_sqrt.real,num_sqrt.imag))