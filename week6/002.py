'''
#文件处理框架，
f = open (fname ,"r")
for line in f:
    #处理数据
f.close()
'''

with open('README.md','r') as f:
    for line in f:
        print(f.read())
