from turtle import *
from datetime import *


def Skip(step):
    # 跨越函数，让turtle画跳跃相对应的间隔，
    penup()
    forward(step)
    pendown()


def mkHand(name, length):
    # 注册Turtle形状，建立表针Turtle
    reset()
    Skip(-length * 0.1)
    begin_poly()
    forward(length * 1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm)


def Init():
    # 初始化整个表盘对象
    global secHand, minHand, hurHand, printer
    # 重置Turtle 并使其指向北
    mode('logo')
    # 建立三个表针，并初始化shape
    mkHand('secHand', 125)
    mkHand('minHand', 130)
    mkHand('hurHand', 90)
    # 初始化Turtle对象
    secHand = Turtle()
    secHand.shape('secHand')
    minHand = Turtle()
    minHand.shape('minHand')

    hurHand = Turtle()
    hurHand.shape('hurHand')

    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 初始化输出文字的Turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()


def SetupClock(radius):
    # 建立表的外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius - 20)
        else:
            dot(5)
            Skip(-radius)
        right(6)


def Week(t):
    week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    return week[t.weekday()]


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d " % (y, m, d)


def Tick():

    # 动态绘制表针，时间间隔为100ms
    t = datetime.today()
    # 时间后的 补数 是来表述该时间占更大单位的份数，
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    # 设置秒针的方向 参数是角度，
    secHand.setheading(6 * second)
    # 设置分针的方向
    minHand.setheading(6 * minute)
    # 设置时针针的方向
    hurHand.setheading(30 * hour)
    #关闭动画效果
    #tracer(False)
    printer.forward(65)
    printer.write(Week(t), align="center", font=("Arial", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center", font=("Arial", 14, "bold"))
    printer.home()
    #tracer(True)
    
    # 100ms之后继续调用tick
    ontimer(Tick, 100)


def main():
    tracer(False)
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()


main()
