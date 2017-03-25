# 使用递归  生成 fib

def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

nnum=int(input("要输出几项？ "))
if nnum <= 0:
    print("请输入正数")
else:
    for i in range(nnum):
        print(fibo(i))