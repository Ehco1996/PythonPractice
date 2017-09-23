'''
已知存在 m x n 大小得方格上有一点p（x,y）

问从原点（0，0）到点p（x，y）有多少种路径
注意！ 每次只能往下或者往右走


用递归得思想去做
每次移动都只有两个选择，
只要把x方向得选择 + y方向得选择
就能够获得最后得答案了！
'''


def findroads(x, y):
    '''
    rtype int
    '''

    if (x - 1 == 0) or (y - 1 == 0):
        return 1
    else:
        return findroads(x - 1, y) + findroads(x, y - 1)


print(findroads(1, 2))

print(findroads(3, 3))

print(findroads(10, 20))
