'''
体育竞技分析
模拟一场体育比赛，通过输入参赛人员的初始能力值和比赛场次，模拟得分 
并计算输出比赛结果
i: 运动员的 能力值 和比赛次数
P: 计算比赛结果
o: 输出结果
'''
import random


def simGame(power_a, power_b, counts):
    '''
    模拟整场比赛，
    counts参数的意思整场比赛的局数
    '''
    score_A = 0
    score_B = 0
    turn = "A"

    # 循环执行每一局比赛
    for i in range(counts):
        if turn == "A":
            if random.random() < power_a:
                score_A += 1
            else:
                turn = "B"
        else:
            if random.random() < power_b:
                score_B += 1
            else:
                turn = "A"

    print("A的分数是：{} B的分数是：{}".format(score_A, score_B))





def main():
    power_a = 0.9
    power_b = 0.5
    counts = 300
    simGame(power_a, power_b, counts)

if __name__ == "__main__":
    main()