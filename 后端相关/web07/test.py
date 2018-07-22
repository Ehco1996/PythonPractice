import hashlib

# 将密码名为转换为bytes对象
pwd = 'xxx'.encode('ascii')

# 创建md5对象
m = hashlib.md5(pwd)

# 返回摘要字符串
print(m.hexdigest())
# e1a570201b2bc050e10f30a78d4aeb29

# 创建sha1对象
s = hashlib.sha256(pwd)

# 返回摘要字符串
print(s.hexdigest())
# 4bf58ecec717e57aecc0d11c53f582aed9ebcb3c
