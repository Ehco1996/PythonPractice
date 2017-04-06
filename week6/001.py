'''
1. 理解文本和二进制打开方式的区别 首先，用文本编辑器生成一个包含“中国是个伟大国家!”的 txt
格式文本文件，命名为 test.txt。编写程序分别用文本文件方式和二 进制文件方式读入，并打印输出效果。
观察输出结果并解释。
'''


# 用绝对目录的方式打开，并用r“只读方式打开文本文件” 用with open 方法使得文件缓存自动清理 ！
with open('/Users/ehco/Documents/codestuff/PythonPractice/week6/test.txt', 'r') as f:
    a = f.read()
    print(a)

#用二进制格式打开！
with open('/Users/ehco/Documents/codestuff/PythonPractice/week6/test.txt', 'rb') as f:
    a = f.read()
    print(a)
