'''
研究一下tushare的接口
学习使用一下DataFrame，数据分析的简单方法
以 顺丰速运 为例



'''

import tushare as ts
import pandas as pd

'''
获取顺丰上市以来的所有股票交易信息
参数表：

date : 交易日期 (index)
open : 开盘价
high : 最高价
close : 收盘价
low : 最低价
volume : 成交量
amount : 成交金额

'''
# 获取原始的dataframe
sf = ts.get_hist_data('002352', start='2017-02-22')

# 为sf加入月份字colums
lis1 = []
# 从data字段截取月份数据，加入list
for i in range(len(sf)):
    lis1.append(sf.index[i][5:7])
# 增加新的字段
sf['month'] = lis1
# 测试数据
print(sf)

# 找到顺丰股票涨的日子,并按照月份统计
increase = sf[sf.close > sf.open]['month'].value_counts()

print('下面是每月涨幅的天数')
print(increase)

# 统计顺丰每个月的成交总量
print(sf.groupby('month')['volume'].sum())

# 统计顺丰每天 收盘价 最高和最低的5天
sorteddf = sf.sort_values('close')
tj = pd.concat([sorteddf[:5], sorteddf[-5:]])
print('收盘价 最高和最低的5天')
print(tj)
