# 通过递归的方式 画出树木，从而更深层次的理解递归


from turtle import Turtle, mainloop


# 画出树木
def tree(plist, l, a, f):
    '''
    plist 是画笔长度大小的集合
    l 是树木分之的长度
    a 是两个分之之间的相差角度
    f 是每次树木减少的长度
    '''
    if l > 5:  # 防止无线递归
        lst = []
        for p in plist:
            p.forward(l)  # 严重当前的方向爬出l具体  左分支
            q = p.clone()  # 复制刚才的绘画，即数的  右分支
            p.left(a)  # 将树枝向左转
            q.right(a)  # 将树枝向右转
            lst.append(p)  # 将p q 加入lst 从而满足下一次的递归调用
            lst.append(q)
        tree(lst, l * f, a, f)


def main():
    p = Turtle()
    p.color('green')
    p.pensize(5)
    p.hideturtle()
    p.speed(100)

    p.left(90)  # 调整画笔的方向 让画笔的笔尖向上

    p.penup()  # 抓起笔头，这样移动的时候就不会留下痕迹
    p.goto(0, -200)  # 设置初始位置，
    p.pendown()  # 将笔头落下，这样就能进行下一次的绘画

    # 初始化树的参数 ，让他画出第一个数
    t = tree([p], 200,65, 0.675)

    return ""


main()
