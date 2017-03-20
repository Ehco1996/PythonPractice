#coding:utf-8
'''
阶乘计算。计算 1+2!+3!+...+10!的结果。
'''

sum = 0
tmp = 1
for i in range(1,11):
    tmp = tmp * i
    sum = sum +tmp

print "运算结果是：%d" %sum