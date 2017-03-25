'''
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
以下代码用于检测用户输入的数字是否为阿姆斯特朗数：
'''

# 获取用户输入的数字
num = str(input("请输入一个数字："))

sum = 0
n =len(num)


temp = int(num)
while temp>0:
    digit  = temp %10
    sum += digit**n
    temp //= 10
if int(num) == sum:
    print(num+'是阿姆斯特朗数')
else:
    print(num+'不是阿姆斯特朗数')
    