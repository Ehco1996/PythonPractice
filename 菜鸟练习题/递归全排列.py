# 通过几个例子来帮助自己理解递归

# 通过递归计算 1 + 2 +3 + 。。。。+n


def add(n):
    if n <= 0:
        return 0
    else:
        return add(n - 1) + n


# python 中递归深度有限，并不能无线递归，因为消耗的资源太大了
n = add(8)
print(n)


# 接受参数n 来打印全文字， 比如接收 123 ，则要打印出 123 132 213 231 312 321

def perm(l):
    if len(l)<=1:
        return[l]
    r = []
    for i in range(len(l)):
        s = l[:i]+l[i+1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i+1]+x)
        
    return r

a = perm("12")

print(a)
