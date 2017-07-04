'''
利用训练好的模型
进行文本相似性分析
'''

import gensim

# 读入训练好的模型
model = gensim.models.Word2Vec.load('qyn.model')



# 我们来找找和范闲类似的人物
print('===============和范闲类似的人物=================')
for s in model.most_similar(positive=['范闲'])[:5]:
    print(s)
print('\n\n')

# 我们来找找武功高强的人物
print('===============武功高强的人物=================')
for s in model.most_similar(positive=['叶流云'])[:5]:
    print(s)
print('\n\n')

# 我们来找到范县的徒弟们
print('===============范闲的徒弟们？=================')
for s in model.most_similar(positive=['杨万里']):
    print(s)
print('\n\n')

# 我们来看一下侯季常到底算不算范闲的徒弟？
print('===============候季常到底真的叛变了？=================')
child = model.most_similar(positive=['杨万里','侯季常'],negative=['范闲'],topn=1)
print(child)
print('\n\n')


# 我们来找一下庆帝的老婆到底是不是范闲她妈？
# 也就是让程序帮我们预测一下叶轻眉在某种意义上是不是庆弟的老妈
print('===============庆帝的真正的老婆=================')
wife = model.most_similar(positive=['范闲','庆帝'],negative=['林婉儿'],topn=1)
print(wife)

