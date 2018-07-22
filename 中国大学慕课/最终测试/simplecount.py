'''
读入一个字符串，内容为英文文章，输入其中出现最多的单词
（仅输入单词，不计算标点符号，同一个单词的大小写形式合并计数），统一以小写输出。

输入格式:
this is a python and Python

输出格式：
python
'''

line = input()
for ch in line:
    if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
        line = line.strip().lower().replace(ch, " ")

wordlist = line.lower().split(' ')
print(wordlist)
dic = {}

for i in wordlist:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

counts = list(dic.items())

counts.sort(key=lambda x: x[1], reverse=True)
print(counts[0][0])
