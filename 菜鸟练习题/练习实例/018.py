# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,
# 特别指出：第0项是0，第1项是第一个1。
# 从第三项开始，每一项都等于前两项之和。

num = int(input("你需要第几项 ？"))

n1 = 0
n2 = 1
count  = 2

while count < num:
    nth = n1 + n2
    print (nth)
    n1 =n2
    n2 = nth
    count += 1

#效率低下
def getANum(index):
    fb = [0, 1]
    a = 0
    b = 1
    for i in range(1, index):
        a = a + b
        fb.append(a)
        b = a + b
        fb.append(b)
    print(fb[index-1])

getANum(num)