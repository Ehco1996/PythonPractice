#coding:utf-8
'''
健康食谱输出。列出 5 种不同的食材，请输出它们可能组成的所 有菜式名称。
'''

diet = ['西红柿','花椰菜','黄瓜','牛排','虾仁']

for x in range(0,5):
    for y in range (5):
        if not(x == y):
            print '%s + %s' %(diet[x],diet[y])