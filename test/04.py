'''
已知一段二进制数据为TCP协议头部信息，写程序解析包含的各字段内容。
TCP Header格式如下 http://www.rfc-editor.org/rfc/rfc793.txt （3.1 Header Format）
'''

import requests

url ='http://www.rfc-editor.org/rfc/rfc793.txt'

r  =requests.get(url)

# 将headers解析为字典形式
header  = dict(r.headers)

print(header)



