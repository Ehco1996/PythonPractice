#素数（prime number）又称质数，有无限个。除了1和它本身以外不再被其他的除数整除。
#以下实例可以输出指定范围内的素数：
# take input from the user
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower,upper + 1):
	# 素数大于 1
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:
			print(num)