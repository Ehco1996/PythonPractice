'''
现假设如下场景：
场面上三只怪:

12/12 大表哥
3/2 杂毛怪

我方：
0/2 嘲讽图腾

问 火山喷发（5费打随机打15）
解掉大表哥的概率是？
'''

import random

# 分别建立三个怪物的血量模型
bigbrother = ['*'] * 12

zamao = ['#', '#']

tuteng = ['$', '$']




def OneTest(hp=[]):
    for i in range(15):
        '''
        模拟15次火山喷发
        每次随机血量减1
        '''
        hp.remove(hp[random.randint(0, len(hp) - 1)])

    return hp


counter = 0

# 开始模拟10000次实验，从而判断概率
for i in range(10000):
    # 构建总的血量池 
    total = bigbrother + zamao + tuteng
    if '*' in OneTest(total):
        counter += 1
        print('大表哥活着')
    else:
        print('大表哥死了')

print("\n\n 大表哥存活的概率是: {}%".format(counter / 10000.0 * 100))

'''
OUT：

大表哥存活的概率是: 75.299%

'''