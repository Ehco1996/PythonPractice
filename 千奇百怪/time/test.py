'''
python time、datetime 模块相关使用的练习
'''

import time
import datetime


# 获取时间戳
t = time.time()
# 格式化时间输出
d = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
print(d)
# 2017-09-22 09:38:27

# 使用datetime模块
date = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
print(date)
# 2017-09-22 09:41:35

# 计算时日期差
d1 = datetime.datetime.now()
# d2 比d1 增加一天
d2 = d1 + datetime.timedelta(days=1)

print(d1,d2)
# 2017-09-22 09:43:22.875839 2017-09-23 09:43:22.875839
print(d1<d2)
# True

# 打印当前日
print(datetime.datetime.now().day)