#以下实例用于判断用户输入的年份是否为闰年：

year = int(input('请输入一个年份 ：'))

if year % 4 == 0:
    if year % 100== 0:
        if year % 400 ==0:
            print ("是闰年") #整年能被400整除的年份是闰年
        else:
            print ("不是闰年")
    else:
        print ("是闰年")
else:
    print ("不是是闰年")