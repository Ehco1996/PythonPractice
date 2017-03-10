#coding:utf-8
'''
整数序列求和，用户输入一个正整数N,计算从1刀N(包含1和N)想加之后的结果
'''

n = raw_input('请输入整数N： \n')
sum = 0

for i in range(int(n)):
    sum += i 
print("从1到N的求和结果是：%d") %sum