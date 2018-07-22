'''
用面向对象的方式
重写001的模拟体育竞技
'''

import random


class PEgame():
    def __init__(self, count, powa, powb):
        self.count = count
        self.powa = powa
        self.powb = powb

    def simGame(self):
        '''
        模拟整场比赛，
        counts参数的意思整场比赛的局数
        '''
        score_A = 0
        score_B = 0
        turn = "A"

        # 循环执行每一局比赛
        for i in range(self.count):
            if turn == "A":
                if random.random() < self.powa:
                    score_A += 1
                else:
                    turn = "B"
            else:
                if random.random() < self.powb:
                    score_B += 1
                else:
                    turn = "A"

        print("A的分数是：{} B的分数是：{}".format(score_A, score_B))


PingPang = PEgame(100, 0.5, 0.1)

PingPang.simGame()
