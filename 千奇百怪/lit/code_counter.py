'''
统计Python代码的行数的小工具
目前只有简单的功能，统计当前目录下所有.py文件的行数
还没有做排除注释等功能。

author: Ehco
'''

import os


def get_filname():
    '''
    返回当前目录下的所有文件的绝对路径名字
    保存在一个列表中返回
    '''

    filename = []
    for root, path, files in os.walk(os.getcwd()):
        for name in files:
            filename.append(os.path.join(root, name))
    return filename


def deal_one_file(file):
    '''
    返回当前文本文件的行数
    '''
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            count = len(lines)
            return count
    except UnicodeDecodeError:
        print('{}这个文件打不开'.format(file))
        return 0
    


code_lines = 0


files = get_filname()

for file in files:
    code_lines += deal_one_file(file)

print(code_lines)
