'''
模拟铅球比赛的面向对象的开发过程
主要是把 game类 比赛类抽象出来
铅球比赛则是其中的一个实例
'''

from math import cos, sin, radians, sqrt


def main():
    angle = 30
    vel = 15
    h0 = 2.0
    #初始化铅球对象
    shot = Projectile(angle, vel, h0)
    time = 0.3
    while shot.getY() >= 0:
        shot.update(time)
    print('\n 铅球飞了{:.2f}m的距离'.format(shot.getX()))


class Projectile():
    def __init__(self, angle, vel, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = vel * cos(theta)
        self.yvel = vel * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        # 本次时间间隔的末速度
        yvel = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel) / 2.0
        # 更新速度
        self.yvel = yvel

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos

main()