'''
通过对 哈姆雷特 小说英文原稿，进行词统计，
其中会利用 dic 类型存储不同单词出现的次数
用list 类型来存储统计结果，
最后用csv 文件进行输出。
'''


# 替换文本文件中的所有标点符号 为“ ” 并将所有字符串变为小写
def replacePunc(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.strip().lower().replace(ch, " ")
    return line

# 处理每一行数据，分离出单词，并将其保存在字典中


def processLine(line, wordcounts):
    # 处理每一行的数据，将其标准化
    line = replacePunc(line)
    # 分离出每个单词 ,每个单词以列表形式保存
    words = line.split()
    # 遍历每个单词，看是否在 单词库中， 如果存在 计数加一，不存在，则创建一个键值对
    for word in words:
        if word in wordcounts:
            wordcounts[word] = wordcounts[word] + 1
        else:
            wordcounts[word] = 1


# 从本机读取文件，并处理，追加成字典，保存在临时字典中。
def CountNmbers(wordcounts):
    with open("./week6/hamlet.txt", 'r') as f:
        for line in f:
            line = replacePunc(line)
            processLine(line, wordcounts)
    return wordcounts


# 排除字的列表
excludes = ['the', 'and']

# 从单词字典里 遍历排除排除列表里的单词


def excludeslist(wordcounts, excludes):
    for ex in excludes:
        if ex in wordcounts.keys():
            del wordcounts[ex]
    return wordcounts



# 初始化存放 单词的字典：
wordcounts = {}
# 调用函数，生成统计每个单词频率的字典 key:单词，value：出现次数
CountNmbers(wordcounts)


# 从列表中排除不想要的字
wordcounts = excludeslist(wordcounts, excludes)

# 生成统计词频的列表，方便排序,
counts = list(wordcounts.items())


# 将列表按照 每一项的第二项排序，
'''
list.sort 方法有两个参数，第一个为key，指向一个迭代累的函数，该函数需要返回用于排序的key值
第二个参数为reverse 类型为boolean 即是否支持反向排序。
这里用了Python3中的新特性 lambda匿名函数，可以迅速返回列表中每一元组的第二项，这里既是单词出现的频率
'''
counts.sort(key=lambda x: x[1], reverse=True)


# 打印出前十个平率出现最高的单词
for i in range(10):
    print(counts[i])


# 将结果写入文件
with open("./week6/hamlet_word.csv", 'w+') as f:
    for i in counts:
        f.write("单词：" + str(i[0]) + ' 次数：' + str(i[1]) + '\n')
