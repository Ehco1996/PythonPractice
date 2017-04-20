'''
题目内容：
当输入字符串结尾是PY时，输出YES，否则输出NO

输入格式:
这是一个字符串PY

输出格式：
YES 或者 NO

输入样例：
这是一个字符串PY

输出样例：
YES
'''

str1 = input()
if str1[-2:]=='PY':
    print('YES')
else:
    print('NO')
