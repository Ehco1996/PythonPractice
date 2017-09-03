'''
已知文本文件，以 \n 为行结束符，
每行包含两个字符串 key和value，
中间用 \t 分割，key和value均有可能重复出现，

输入文件内容格式举例：  
 
2687694 18070300
2687694 18070300
2687694 18070500
2687694 18070500
2687697 15050000
2687697 15050000
2687697 15050500
2687697 15050500  
 
请写程序统计下列信息：
1） 每个key对应多少不同的唯一value？
2） 每个不同的value出现次数是多少？  
并按value次数从大到小输出结果文件
(key1:value1,count1;value2,count2....\n
key2:value1,count1;value2,count2....)
 
输出文件格式举例：  
 
2687694:18070300,2;18070500,2
2687697:15050000,2;15050500,2
'''

data = '''2687694\t18070300
2687694\t18070300
2687694\t18070500
2687694\t18070500
2687697\t15050000
2687697\t15050000
2687697\t15050500
2687697\t15050500  
'''

# 先将数据按行分类
data_list = data.splitlines()

# 建立keys字典
dicts = {}

# 遍历数据 构建符合格式要求的字典
for data in data_list:
    k = data.split('\t')[0].strip()
    v = data.split('\t')[1].strip()
    # 判断记录是否在字典里
    if k not in dicts:
        dicts[k] = {v: 1}
    else:
        if v not in dicts[k]:
            dicts[k][v] = 1
        else:
            dicts[k][v] += 1


# 将数据格式化输出
for k, v in dicts.items():
    # 打印k
    print(k, end=':')
    # 获取v_dict 的长度
    lens = len(v)
    i = 0
    # 将count值排序
    sorted(v.items(), key=lambda item: item[1], reverse=True)
    for name, c in v.items():
        i += 1
        print('{},{}'.format(name, c), end=';')
        # 格式化输出，换行
        if i == lens:
            print('')
