'''
设定一个长度为N的数字字符串，将其分为两个部分，找出一个切分位置使得两部分的乘积最大
比如 123 ==  12 x 3 = 36 
'''

# 递归求全排列


def perm(l):
    if len(l) <= 1:
        return[l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i + 1] + x)

    return r


def max_pNum(num):
    res = []
    r = perm(num)
    for nu in r:
        for i in range(1, len(nu)):
            ans = int(nu[0:i]) * int(nu[i:])
            res.append(ans)
    print(max(res))


max_pNum('123456')
