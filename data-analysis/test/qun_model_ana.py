'''
利用gensim机器学习模块
训练庆余年小说模型
'''
import gensim


# 导入我们利用结巴分词后的结果
with open('result.txt') as f:
    wordslist = list(word.strip() for word in f.readlines())


# 开始训练模型
print('开始训练模型。。。这个时间很长，去喝杯咖啡吧')
model = gensim.models.Word2Vec(
    wordslist, size=100, window=5, min_count=4, workers=4)
print('训练完毕。正在将模型保存到本地')
model.save('qyn.model')
print('Okey ')
