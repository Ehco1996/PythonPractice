'''
寻找第n个默尼森数。
代码格式如下：
def prime(num):
    ...
def monisen(no):
    … …
    return  xxx

print(monisen(int(input())))    #此处不需要自己输入，只要写这样一条语句即可，主要完成monisen()函数（4分）
经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
输入格式:按提示用input()函数输入
输出格式：int类型
输入样例：4
输出样例：127

'''


def prime(num):
    '''
    判断是否是素数
    '''
    if num < 2:
        return False
    elif num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def monisen(no):
    '''
    找到第no个莫尼森数
    '''

    num = []
    i = 2
    while True:
        if len(num) <no:
            if prime(i):
                mo = 2 ** i - 1
                if prime(mo):
                    num.append(mo)
                    i += 1
                else:
                    i += 1
            else:
                i += 1
        elif len(num) == no:
            return(num[no - 1])



print(monisen(int(input())))
