#下面代码实现了最大公约数的算法

def hcf(x,y):
    if x >y:
        sm = y
    else:
        sm = x
    
    for i in range(1,sm+1):
        if ((x%i==0) and (y%i==0)):
            hcf = i
    return hcf

# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print( num1,"和", num2,"的最大公约数为", hcf(num1, num2))