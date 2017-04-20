'''
题目内容：
将输入的字符串垂直输出

输入格式:
这是一个字符串

输出格式：
这
是
一
个
字
符
串

输入样例：
中英文String

输出样例：
中
英
文
S
t
r
i
n
g
'''

str1 = input()
list1 =[]
for i in str1:
    list1.append(i)

for i in list1:
    print(i) 