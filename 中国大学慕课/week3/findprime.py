'''
题目内容：
我们认为2是第一个素数，3是第二个素数，5是第三个素数，依次类推。
现在，给定两个整数n和m，0<n<=m<=200，你的程序要计算第n个素数到第m个素数之间所有的素数的和，包括第n个素数和第m个素数。
注意，是第n个素数到第m个素数之间的所有的素数，并不是n和m之间的所有的素数。
'''

n = int(input("输入第一个数： "))
m = int(input("输入第一个数： "))



def isprime(num):
    if num > 1:
        for i in range(2, num - 1):
            if num % i == 0:
                return False
    else:
        return False
    return True


'''
#记录素数序号
count = 0
i = 1
sum = 0

#思路一解题
while count<=m:
    while (i!= 0):
        if isprime(i):
            count += 1
            if n <= count and count <= m:
                sum = sum + i 
                i += 1
            elif count > m:
                i = 0
            else:
                i += 1
        else:
            i+=1
print (sum)
'''

'''
## 第二种解题思路
# 素数集合
snum = []
s = 2
# 找出小于m的素数
while len(snum) <= m:
    if isprime(s):
        snum.append(s)
        s += 1
    else:
        s += 1
# 打印素数集合
print(snum)

add = 0
for i in range(n, m + 1):
    add += snum[i - 1]

print(add)
'''

# 第三种解题思路 不用函数
# 开始寻找素数
count = 0
sum = 0
# 初始的素数
num = 2


while count <= m:
    if num == 2 or num == 3:
        count += 1
        if n <= count and count <= m:
            sum += num
            num += 1
        else:
            num += 1

    else:
        for i in range(2, num - 1):
            if num % i == 0:
                num += 1
                break
        else:

            count += 1
            if n <= count and count <= m:
                sum += num
                num += 1
            else:
                num += 1
print(sum)
