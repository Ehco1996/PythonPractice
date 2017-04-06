'''
通过第三方结巴分词库，
做到中文小说的词语统计
通过wordcloud 生成图云。
'''

import jieba


# 去掉中文字符里的所有标点符号，以及空格
def replacePunc(line):
    for ch in line:
        if ch in"，。.、？：“、！@#￥%……&*（）——+~\n《》<>”:;()":
            line = line.strip().replace(ch, '')
    return line


def processLine(line, wordcounts):
    # 分离每一行数据，将其标准化
    line = replacePunc(line)
    # 利用结巴分词，分出该行中的每一个中文词语，结果保存在临时列表中
    words = jieba.lcut(line)
    # 开始遍历每一个中文词语，如果不存在，就在wordcounts字典中新增值，如果存在就在基础上累加1
    for word in words:
        if word in wordcounts:
            wordcounts[word] = wordcounts[word] + 1
        else:
            wordcounts[word] = 1


# 去除结巴分词出的单个汉字
def excludesOne(wordcounts):
    for x in list(wordcounts):
        if len(x) <= 1:
            del wordcounts[x]
    return wordcounts

# 调用之前写好的函数，来生成保存词频的字典


def start_pro(wordcounts):
    with open('./week6/择天记.txt', 'r') as f:
        for line in f:
            line = replacePunc(line)
            processLine(line, wordcounts)
    return wordcounts


# 将结果写入文件
def outFile(counts):
    with open('./week6/择天记_count.txt', 'w+') as f:
        for i in counts:
            f.write(str(i) + '\n')



def main():
    # 初始化临时保存词频的字典
    wordcounts = {}
    # 开始项目
    start_pro(wordcounts)
    # 删除单个字的词语
    wordcounts = excludesOne(wordcounts)
    # 生成列表，方便排序
    counts = list(wordcounts.items())
    # 通过列表的元组的第二项（词频）来进行排序
    counts.sort(key=lambda x: x[1], reverse=True)
