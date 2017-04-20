'''
题目内容：
实现一个凯撒密码的变种算法，对输入字符串进行加解密处理
把字母a-z分别循环对应为相距13个位置的字母n-m，即
原文字母：a b c d e f g h i j k l m n o p q r s t u v w x y z
对应字母：n o p q r s t u v w x y z a b c d e f g h i j k l m
大写字母对应方式与小写字母类似，其他符号（含标点符号）不作处理

输入格式:
一个英文字符串

输出格式：
经过上述算法加密的字符串

输入样例：
The Zen of Python

输出样例：
Gur Mra bs Clguba

'''
ortext = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ortext_up = []
for i in ortext:
    ortext_up.append(i.upper())


str1 = str(input())

text = str1.split(' ')


for word in text:
    for char in word:
        if char in ortext:
            i = ortext.index(char)
            if i > 12:
                i = i + 13 - 26
                print(ortext[i], end='')
            else:
                i = i + 13
                print(ortext[i], end='')
    
        elif char in ortext_up:
            i = ortext_up.index(char)
            if i > 12:
                i = i + 13 - 26
                print(ortext_up[i], end='')
            else:
                i = i + 13
                print(ortext_up[i], end='')

        else:
            print(char, end=' ')
    else:
        print(' ', end='')

else:
    print()
