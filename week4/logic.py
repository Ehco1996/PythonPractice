'''
请分析下面程序，若输入 score 为 80，输出 grade 为多少?
是否符合逻辑，为什么?
'''
score = 99
if score >= 60.0:
    print("D")
elif score >= 70.0:
    print("C")    
elif score >= 80.0:
    print("B")
else:
    print("A")
    
'''
明显不符合判断，if语句是顺序执行
当score = 80时
就会满足第一个条件，那么就会调出循环
下面是改进后的版本
'''
score = 80
if 70>score >= 60.0:
    print("D")
elif 80>score >= 70.0:
    print("C")    
elif 90>score >= 80.0:
    print("B")
elif score>90:
    print("A")
    
