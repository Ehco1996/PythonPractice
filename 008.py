#coding:utf-8
'''
太阳花的绘制。绘制一个太阳花的图形，如图所示。
'''

from turtle import *

color('red','yellow')
begin_fill()
while 1:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        delay()

end_fill()
done()