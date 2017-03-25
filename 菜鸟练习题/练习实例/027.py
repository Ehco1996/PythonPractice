# python 的文件io 包括 open read write

#写文件 用with open 特性 可以防止忘记关闭文件
with open('test.txt','wt') as f:
    f.write("测试文本\n hahahha")

#读文件：
with open('test.txt','rt') as f:
    text = f.read()

print(text)