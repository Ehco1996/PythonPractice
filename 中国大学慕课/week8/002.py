'''
使用Turtle库绘制一朵玫瑰花，形状不限
🌹
'''

from turtle import *
def curvemove():
    for i in range(180):
        right(1)
        forward(1)



def darw(angle):
    color('green','pink')
    begin_fill()
    left(angle)
    forward(111.65)
    curvemove()
    goto(0,0)
    end_fill()
for i in range(0,288,15): 
    tracer(False)
    darw(i)
    tracer(True)

setheading(-90)
pensize(5)
color ('green')
forward(300)

done()
