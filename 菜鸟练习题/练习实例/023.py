#最小公倍数的实现

def lcm(x,y):
    if x > y:
        large = x
    else:
        large = y

    while True:
        if ((large%x == 0)and(large%y ==0)):
            lcm = large
            break
        large  += 1
    return lcm    
    
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print( num1,"和", num2,"的最小公倍数为", lcm(num1, num2)) 