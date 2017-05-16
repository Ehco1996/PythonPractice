'''
计算显示器面积

输入： 对角线inch 比例int 
输出： 长cm 宽cm 面积cm2
'''

import math

diagonal = eval(input("请输入显示器尺寸： （单位：inch）"))

long = eval(input("请输入显示器长的比例： （例如 16）"))

width = eval(input("请输入显示器宽的比例： （例如 9）"))

# 对角线的平方
x = (diagonal * 2.54)**2
# 边长因子
yz = math.sqrt(x / (long**2 + width**2))


print("显示器的长:{:.2f}cm  \n显示器的宽：{:.2f}cm\n显示器的面积：{:.2f}cm2" .format(
    long * yz, width * yz, long * yz * width * yz))
