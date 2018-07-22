#coding:utf-8
'''
螺旋线绘制。绘制一个螺旋线的图形，如图所示。
'''
import turtle
import time

turtle.speed('fastest')
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)