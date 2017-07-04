'''
通过结巴分词和gensim来分析庆余年中的人物和角色关系
'''


# 从百度百科下载的文中的人物名字，并筛选出重复的名字，保存在列表里
with open('name.txt', 'r') as f:
    names = list(set(name.strip() for name in f.readlines()))

# 读入整个庆余年文本的内容：
with open('001.txt', 'r', encoding='gbk') as f:
    content = list(line.strip() for line in f.readlines())


# 我们从最简单的做起，统计人物出先次数：
def find_pepple_showup_cont(num=10):
    '''
    对比统计人物姓名出现的次数，
    并返回出现次数最多的前Num个人
    '''
    novel = ''.join(content)
    showup_counts = []
    for name in names:
        # 这里从文章统计处每个名词出现的次数后，保存在一个列表里返回
        showup_counts.append([name, novel.count(name)])
    # 我们将列表通过出现次数排序
    showup_counts.sort(key=lambda v: v[1], reverse=True)

    return showup_counts[:num]


'''
# 简单的展示一下数据
showup_10 = find_pepple_showup_cont()
print(showup_10)

# 用DataFrame展示：
import pandas as pd
show = pd.DataFrame(showup_10, columns=['names', 'counts'])
print(show)

# 用matplotlib绘制直方图展示：
import matplotlib.pyplot as plt
from pylab import mpl
# 设置中文子字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 展示的姓名和数据
data = list(show.counts)
index = list(show.names)
# 绘制直方图
plt.bar(range(len(data)), data, tick_label=index)
plt.xlabel('出现的人物')
plt.ylabel('出现的次数')
plt.title('庆余年人物出现频次图')
plt.savefig('rwpc.jpg')
plt.show()
'''

# 利用结巴分词来进行中文分词
import jieba
import jieba.analyse
import matplotlib.pyplot as plt


# 获取关键词 最多的二十个
print('正在分析文章中的关键词！')
tags = jieba.analyse.extract_tags(' '.join(content), topK=20, withWeight=True)
print('关键词:')
for k, v in tags:
    print('关键词：{}   权重：{:.3f}'.format(k, v))

'''
# 利用关键词制作图云：
from wordcloud import WordCloud
txt = ''.join([v + ',' for v, x in tags])
wordcloud = WordCloud(background_color='white',
                      font_path='cn.ttf', max_font_size=40).generate(txt)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('qun_gjc.jpg')
'''

# 将关键词加入结巴分词
for tag, x in tags:
    jieba.add_word(tag)

# 将小说中的姓名加入结巴分词的关键词
for name in names:
    jieba.add_word(name)

# 加入中文停用词列表
with open('stopwords.txt', 'r') as f:
    STOPWORD = [word.strip() for word in f.readlines()]

# 开始进行分词
print('开始进行分词。。。。')
# 我们期待的分词结果是保存着小说每一句话的分词结果
# 即一个二元数组，这将方便我们一会进行模型的训练
sentence = []
for line in content:
    seg_list = list(jieba.cut(line, cut_all=False))
    unique_list = []
    # 开始去除停用词
    for seg in seg_list:
        if seg not in STOPWORD:
            unique_list.append(seg)
    sentence.append(unique_list)
print('分词完毕')


# 开始训练模型
import gensim
# Gensim中的Word2Vec期望的输入是经过分词的 句子列表。即是一个包含句子分词结果的二维数组
print('开始训练模型。。。这个时间很长，去喝杯咖啡吧')
model = gensim.models.Word2Vec(
    sentence, size=100, window=5, min_count=4, workers=4)
print('训练完毕。正在将模型保存到本地')
model.save('qyn.model')
print('Okey ')
