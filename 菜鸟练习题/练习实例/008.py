#交换两个变量的值

x = float(input("请输入 x 的值："))
y = float(input("请输入 y 的值："))

# 方案一 通过 temp变量交换
temp = x
x = y
y = temp
print ("x: %f y: %f" % (x,y))

#方案二 数学技巧
x = x + y
y = x - y
x = x - y
print ("x: %f y: %f" % (x,y))

#方案三 Python3 新特性
x,y = y,x

print ("x: %f y: %f" % (x,y))