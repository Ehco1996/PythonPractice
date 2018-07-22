'''
已知如下序列：[(1,{"date":"2015-3-1"},"jack"),(2,{"date":"2015-3-2"},"tom")...]，写程序根据date先后排序。
'''


data = [
    (1, {"date": "2015-3-3"}, "jack"),
    (2, {"date": "2015-3-2"}, "tom"),
]


def date(s):
    return s[1]['date']


sorted_date = sorted(data, key=date)
print(sorted_date)
