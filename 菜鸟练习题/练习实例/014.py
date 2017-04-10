 #对于质数与素数的判断
'''
一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），
换句话说就是该数除了1和它本身以外不再有其他的因数。
'''
num = int(input("请输入一个数字: "))

#质数大于一
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num,"不是质数")
            break
    else:
        print(num,"是 质数")
else:
    print(num,"不是质数")
