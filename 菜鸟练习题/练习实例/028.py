#python 中的字符串属性的判断

#测试一
print("测试实例一")
str = "ehcospeed.com"
print(str.isalnum()) # 判断所有字符都是数字或者字母
print(str.isalpha()) # 判断所有字符都是字母
print(str.isdigit()) # 判断所有字符都是数字
print(str.islower()) # 判断所有字符都是小写
print(str.isupper()) # 判断所有字符都是大写
print(str.istitle()) # 判断所有单词都是首字母大写，像标题
print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

print("------------------------")


#测试二
print("测试实例二")
str = "zhouhao! sadasd ZHouhao"
print(str.isalnum()) 
print(str.isalpha()) 
print(str.isdigit()) 
print(str.islower()) 
print(str.isupper()) 
print(str.istitle()) 
print(str.isspace()) 