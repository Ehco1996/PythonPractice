'''
有5名某界大佬xiaoyun、xiaohong、xiaoteng、xiaoyi和xiaoyang，
其QQ号分别是88888、5555555、11111、12341234和1212121，
用字典将这些数据组织起来。
编程实现以下功能：用户输入某一个大佬的姓名后输出其QQ号，
如果输入的姓名不在字典中则输出字符串“Not Found”。
'''

def find_person(dict1, user):
     if user in dict1:
          return dict1[user]
     else:
          return 'Not Found'





if __name__ == "__main__":
     dalao = {'xiaoyun':'88888','xiaohong':'5555555','xiaoteng':'11111','xiaoyi':'12341234',
               'xiaoyang':'1212121'}
     strU =  input()
     print(find_person(dalao, strU))