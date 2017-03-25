# python 中的list常规用法

# 生成一个空的列表
list1 = []

# list 可以用append的方法往后添加一个元素
list1.append("1")
list1.append('2')
list1.append('a')

print(list1)

# list可以用sort方法进行排序，用reverse方法进行反转
list1.sort()
print(list1)
list1.reverse()
print(list1)

# 通过下标[开始位置:结束位置]进行切片操作
list2 = list1[1:2]
print(list2)

# 增加元素的其他方法 指定位添加 和在末尾扩展
list1.insert(-1, "sss")
list1.extend(['asd', '123'])
print(list1)

# 列表中的搜索位置
print(list1.index("a"))

# 删除元素 删除首次出现的元素
list1.remove("asd")
# pop会删除最后一个原色 返回新的列表
list1.pop()
print(list1)

# 使用jion 连接list成为字符串
params = {"server": "mpilgrim", "database": "master",
          "uid": "sa", "pwd": "secret"}
a = ["%s=%s" % (k, v) for k, v in params.items()]
print(a)

# 字符串的分割
s = ';'.join(params)
print(s)
s1 = s.split(";")
print(s1)

# list 中的映射解析
li = [1, 2, 3, 4]
li1 = [a * 2 for a in li]
print(li1)

# list的过滤
li2 = [x for x in li if x > 2]
print(li2)

# 字典的解析：
print(params.keys())
print(params.values())
print(params.items())

for k, v in params.items():
    print(k, v)
