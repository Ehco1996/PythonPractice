# 用 if elif  else 条件语句 来判断数字是正数 负数 还是零

num = float(input("请输入一个数字 ："))

if num > 0:
    print("是个正数")
elif num == 0:
    print("是零")
else:
    print("负数")