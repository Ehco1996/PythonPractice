"""
2017/03/01

web 7 预习内容, 都是理论知识, 随便看看, 以上课为准


1, 摘要算法/用处/常见套路
摘要算法是一种能产生特殊输出格式的算法
给定任意长度的数据生成定长的密文
摘要结果是不可逆的, 不能被还原为原数据
理论上无法通过反向运算取得原数据内容
通常只被用来做数据完整性验证
或者是用来加密用户密码

常用的摘要算法主要有 md5 和 sha1
md5 的输出结果为 32 字符
sha1 的输出结果为 40 字符

用法如下见 models.py 里的 User 类

import hashlib
# 要加密的是 'gua'
# 用 ascii 编码转换成 bytes 对象
pwd = 'gua'.encode('ascii')
# 创建 md5 对象
m = hashlib.md5(pwd)
# 返回摘要字符串, 这里是 c9c1ebed56b2efee7844b4158905d845
print(m.hexdigest())
#
# 创建 sha1 对象
s = hashlib.sha1(pwd)
# 返回摘要字符串, 这里是 4843c628d74aa10769eb21b832f00a778db8b17e
print(s.hexdigest())





2, 用 md5 或者 sha1 保护用户的密码
用户的密码存在数据库中, 有可能会被黑客盗取(拖库)
所以一般会对用户的密码使用摘要算法加密
存储在数据库中的是加密后的密文
(所以找回密码是不可能的, 只能重置, 因为摘要不可逆)




3, 用 salt 防止黑客对密码进行碰撞
假如用户使用简单密码, 破解者可以用提前生成的简单密码摘要表(彩虹表)
来破解原文
所以我们会存储一个额外的信息, 扰乱用户的简单密码
(具体的上课会详细解释)

使用如下函数可以生成一个带盐的密文
def salted_password(self, password, salt):
    def md5hex(ascii_str):
        return hashlib.md5(ascii_str.encode('ascii')).hexdigest()
    hash1 = md5hex(password)
    hash2 = md5hex(hash1 + salt)
    return hash2




4, 作业 6 中描述的数据存储结构



5, 实现一个微博程序, 和之前 todo 程序的不同之处是带有评论功能
"""
