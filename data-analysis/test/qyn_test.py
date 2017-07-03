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
