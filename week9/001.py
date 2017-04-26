'''
利用Python 内置os库来对操作系统的的文件进行批量修改。
'''

import os

# 获取当前目录
base_path = os.getcwd()
print('当前目录是：', base_path)


def makefiles(path):
    for i in range(1, 20):
        f = open(path + str(i) + '.txt', 'w+')
        f.writelines('')
        f.close()
    print('所有文件空文件书写完毕')

# 在桌面test文件夹创建20个等待处理的实验文件
# makefiles('/Users/ehco/Desktop/test/')

#批量修改文件名字
def RnameAllfile(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            # 分离文件名和扩展名
            fname, fext = os.path.splitext(name)
            # 修改文件名
            os.rename(os.path.join(root, name),
                      os.path.join(root, fname + '_py' + fext))


RnameAllfile('/Users/ehco/Desktop/test/')
