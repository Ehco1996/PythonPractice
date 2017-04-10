'''
题目内容：
每个非素数（合数）都可以写成几个素数（也可称为质数）相乘的形式，这几个素数就都叫做这个合数的质因数。比如，6可以被分解为2x3，而24可以被分解为2x2x2x3。
现在，你的程序要读入一个[2,100000]范围内的整数，然后输出它的质因数分解式；当读到的就是素数时，输出它本身。

输入格式:
一个整数，范围在[2,100000]内。

输出格式：
形如：
n=axbxcxd
或
n=n
所有的符号之间都没有空格，x是小写字母x。

输入样例：
18

输出样例：
18=2x3x3

'''


#判断是否是素数
def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
            break
    return True




def res(num):
    #首先判断是否是素数，如果是的话直接输出 如果不是就打印表头，并开始分解因式
    if isPrime(num):
        print("{}={}".format(num, num))
    else:
        print("{}=".format(num), end='')

        while(not(isPrime(num))):
            #当这个数部署素数的时候，开始寻找第一个能被他整除的素数因式，当找到这个素数因式的的时候，打印出这个因式，并更新原本的数，将其更新为整除完之后数，再次寻找因式
            for i in range(2, num):
                if num % i == 0 and isPrime(i):
                    print("{}x".format(i), end='')
                    num = num // i
                    break
        print(num)


res(100)
