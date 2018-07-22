'''
基于 MovieLens 100k 
数据集中男性女性对电影的评分来判断男性还是女性电影 
评分的差异性更大


u.data 表示 100k 条评分记录，每一列的数值含义是: user id | item id | rating | timestamp
u.user 表示用户的信息，每一列的数值含义是:
user id | age | gender | occupation | zip code
'''

import pandas as pd
import numpy as np

# 读入数据
unames = ['user id', 'age', 'gender', 'occupation', 'zip code']
users = pd.read_table('mk-100k/u.user', sep='\|',
                      names=unames, engine='python')
# print(users)
rnames = ['user id', 'item id', 'rating', 'timestamp']
ratings = pd.read_table('mk-100k/u.data', sep='\t',
                        names=rnames, engine='python')
# print(ratings)
# 选择需要的数据列，提高效率

users_df = pd.DataFrame()
users_df['user id'] = users['user id']
users_df['gender'] = users['gender']
ratings_df = pd.DataFrame()
ratings_df['user id'] = ratings['user id']
ratings_df['rating'] = ratings['rating']

print(users_df)

print(ratings_df)

# 将数据合并
ratings_df = pd.merge(users_df, ratings_df)
# 利用pandas中的数据透视表 pivot_table（）函数对数据进行聚合）
gender_table = pd.pivot_table(
    ratings_df, index=['gender', 'user id'], values='rating')
print(gender_table)
gender_df = pd.DataFrame(gender_table)
print(gender_df)

# 区分男女
Female_df = gender_df.query("gender==['F']")
Male_df = gender_df.query("gender==['M']")

# 按照性别计算评分的标准差
Female_std = np.std(Female_df)
Male_std =np.std(Male_df)
# 输出结果
print ('Gender:\n男性{:.6f}\n女性{:.6f}'.format(Male_std.rating,Female_std.rating))

# 结论，女性的电影评分差距更大