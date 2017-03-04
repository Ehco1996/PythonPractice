#coding:utf-8
'''
九九乘法表输出：工整的打印出常用的九九乘法表，格式不限
'''

for i in range(1,10):
    for j in range(1,10):
        print "%d * %d = %d \n" %(j,i,j * i)
