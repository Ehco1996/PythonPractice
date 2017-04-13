'''
模拟铅球比赛的结果：
I： 初始高度height ， 初始速度speed ，初始的角度angle
P：  计算出铅球的速度在x轴y轴的速度，（这里需要引入math库的sin cos 以及将 角度转换弧度的函数 radians ，
   接着通过重力加速度 9.8 m/s 计算 整个运动的过程的时间， 在利用时间算出水平分量上运动的距离
O: 输出 飞行时间 以及 飞行距离
'''

from math import cos, sin, radians,sqrt


def simGame(height, speed, theta):
    #初始化速度在xy轴上的分量
    x_speed = speed * cos(theta)
    y_speed = speed * sin(theta)
    # 计算求的最高位置
    max_height = height + y_speed/2*y_speed/9.8
    #计算运动时间 h = 0.5gt2
    t = sqrt(max_height*2/9.8)
    end = x_speed * t  
    print("一共运动了：{:.2f}s 飞行的距离是：{:.2f}m".format(t,end))


def main():
    height = 2.0
    speed = 15
    #将角度转换为弧度，以便于cos sin 函数使用
    theta = radians(30)
    simGame(height,speed,theta)
    
main()
 