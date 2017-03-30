import turtle
import time
'''
引入turtle图形库，绘制‘七段数码管’
并且显示出当前的系统日期

'''

# 引用turtle对象
p = turtle.Turtle()
# 设置画笔粗细
p.pensize(5)
# 影藏小龟的箭头
p.hideturtle()
# 设置爬行速度
p.speed(3)

#将起点向左移动
p.penup()
p.left(180)
p.forward(450)
p.left(180)



# 向左偏向angle度，画出一笔的长度 可扩展


def draw(angle=0):
    p.left(angle)
    p.forward(50)

# 画出文字间隙


def drawBlank():
    p.penup()
    p.forward(50)
    p.pendown()

# 将画笔置于下一个数字的左下角
# def drawback:


# 画出数字0
def draw0():
    draw()
    draw(90)
    draw()
    draw(90)
    draw(90)
    draw()
    # 将箭头位置偏向右方
    p.left(90)
    # 将箭头移到下一个起点位置
    drawBlank()
    drawBlank()


# 画出数字1
def draw1():
    drawBlank()
    draw(90)
    draw()
    # 将画笔调入下一个位置
    p.left(180)
    draw()
    draw()
    p.left(90)
    drawBlank()


def draw2():
    draw()
    p.left(180)
    draw()
    draw(270)
    draw(270)
    draw(90)
    draw(90)
    # 将画笔调入下一个位置
    p.left(180)
    drawBlank()
    drawBlank()
    p.right(90)
    drawBlank()
    drawBlank()
    p.left(90)


def draw3():
    draw()
    draw(90)
    draw(90)
    p.left(180)
    draw()
    p.left(90)
    draw()
    draw(90)
    # 将画笔调入下一个位置
    p.left(180)
    drawBlank()
    drawBlank()
    p.right(90)
    drawBlank()
    drawBlank()
    p.left(90)


def draw4():
    drawBlank()
    draw(90)
    draw()
    p.left(180)
    draw()
    draw(270)
    draw(270)
    # 将画笔调入下一个位置
    p.left(270)
    drawBlank()
    drawBlank()
    p.right(90)
    drawBlank()
    drawBlank()
    p.left(90)


def draw5():
    draw()
    draw(90)
    draw(90)
    draw(270)
    draw(270)
    # 将画笔调入下一个位置
    drawBlank()
    p.right(90)
    drawBlank()
    drawBlank()
    p.left(90)


def draw6():
    draw()
    draw(90)
    draw(90)
    draw(90)
    p.left(180)
    draw()
    draw()
    draw(270)
    # 将画笔调入下一个位置
    drawBlank()
    p.right(90)
    drawBlank()
    drawBlank()
    p.left(90)


def draw7():
    drawBlank()
    draw(90)
    draw()
    draw(90)
    # 将画笔调入下一个位置
    p.left(180)
    drawBlank()
    drawBlank()
    p.right(90)
    drawBlank()
    drawBlank()
    p.left(90)


def draw8():
    draw()
    draw(90)
    draw()
    draw(90)
    draw(90)
    draw(90)
    p.left(180)
    draw()
    draw(90)
    # 将画笔调入下一个位置
    draw(90)
    drawBlank()


def draw9():
    drawBlank()
    draw(90)
    draw(90)
    draw(270)
    draw(270)
    draw(270)
    # 将画笔调入下一个位置
    drawBlank()
    p.left(90)
    drawBlank()


# 装着函数的列表
app = [draw0, draw1, draw2, draw3, draw4, draw5, draw6, draw7, draw8, draw9]



date = str(input("请输入日期，格式为YYYY/MM/DD :"))

for i in date:
   app[int(i)]()

time.sleep(3)

