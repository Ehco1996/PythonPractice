# 公钥、私钥
服务器上存公钥
本机上存私钥

每次请求登录时，通过非对称加密的技术来核对私钥
如果通过则可以登录

# 部分原理

私钥 > 公钥

互为密码互相加密技术

# RSA算法(三名科学家名字)

# linux服务器配置


## 安装ufw快速配置iptables

yum install ufw
ufw allow 22
ufw allow 80
ufw allow 443
ufw default deny incoming
ufw default allow outgoing
ufw status verbose  
ufw enable


# ===
# 服务器中文编码问题
# ===
# 
# 编辑下面的文件, 不要拼错
nano /etc/environment
# 加入下面的内容, 保存退出
LC_CTYPE="en_US.UTF-8"
LC_ALL="en_US.UTF-8"
