'''
定义函数countchar()统计字符串中所有出现的字母的个数（允许输入大写字符，并且计数时不区分大小写）。形如：
def countchar(str):
      ... ...
     return a list
if __name__ == "__main__":
     str = input()
     ... ...
     print(countchar(str))
输入格式:
字符串

输出格式：
列表

输入样例：
Hello, World!

输出样例：
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
'''

def countchar(str):
    # 生成26个字母的列表
    a = [chr(i) for i in range(97,123)]
    # 将列表转换为hash表
    dic = {}
    for char in a:
        dic[char]=0

    # 将遍历过的值返回
    for i in str:
        if i in dic.keys():
            dic[i] += 1
    
    return list(dic.values())

if __name__ == "__main__":
     str1 = str(input()).lower()
     
     print(countchar(str1))