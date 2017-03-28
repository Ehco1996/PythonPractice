'''
1多项式加法（5分）
题目内容：
一个多项式可以表达为x的各次幂与系数乘积的和，比如：
2x6+3x5+12x3+6x+20
现在，你的程序要读入两个多项式，然后输出这两个多项式的和，也就是把对应的幂上的系数相加然后输出。
程序要处理的幂最大为100。

输入格式:
总共要输入两个多项式，每个多项式的输入格式如下：
每行输入两个数字，第一个表示幂次，第二个表示该幂次的系数，所有的系数都是整数。第一行一定是最高幂，最后一行一定是0次幂。
注意第一行和最后一行之间不一定按照幂次降低顺序排列；如果某个幂次的系数为0，就不出现在输入数据中了；0次幂的系数为0时还是会出现在输入数据中。

输出格式：
从最高幂开始依次降到0幂，如：
2x6+3x5+12x3-6x+20
注意其中的x是小写字母x，而且所有的符号之间都没有空格，如果某个幂的系数为0则不需要有那项。

输入样例：
6 2
5 3
3 12
1 6
0 20
6 2
5 3
2 12
1 6
0 20

输出样例：
4x6+6x5+12x3+12x2+12x+40
'''

#初始化存储器
num1 = []
num2 = []
max = 0

print("请开始输入第一个多项式")
a = int(input("输入的幂数"))
b = int(input("输入幂的系数"))
# 生成num1 二项数列
for i in range(0, a + 1):
    num1.append(0)
num1[a] = b

while True:
    a = int(input("输入的幂数"))
    b = int(input("输入幂的系数"))
    num1[a] = b
    if a == 0:
        num1[a] = b
        print("输入完毕")
        break

print(num1)#输出第一个多项式 0 表示该地i次幂的系数为零


print("请开始输入第二个多项式")

a = int(input("输入的幂数"))
b = int(input("输入幂的系数"))
# 生成num1 二项数列
for i in range(0, a + 1):
    num2.append(0)
num2[a] = b

while True:
    a = int(input("输入的幂数"))
    b = int(input("输入幂的系数"))
    num2[a] = b
    if a == 0:
        num2[a] = b
        print("输入完毕")
        break

print(num2)#输出第二个多项式 0 表示该地i次幂的系数为零

# 取出最大的判断列表数量

if len(num1) <= len(num2):
    max = len(num1)
else:
    max = len(num2)


#获取循环次数
i = max
while i >=0:
    sum = 0
    if i < max and num1[i] != 0:
        sum += num1[i]
    if i < max and num2[i] != 0: #将两个多项式的同幂系数合并
        sum += num2[i]
    if sum == 0: #幂数为0是的情况
        i = i -1
        continue

    if i > 1:
        print(str(sum) + "x" +str(i)+ "+",end='')
    elif i == 1:
        print(str(sum) + "x" + "+",end='')
    elif i == 0:
        print(str(sum))
    i = i - 1