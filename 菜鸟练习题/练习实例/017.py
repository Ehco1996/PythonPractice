#下面实例实现了如何实现九九乘法表

for i in range(1,10):
    for j in range(1,10):
        print("{}乘以{} = {}".format(i,j,i*j),end=' ')