#Python版smtp 模块练习

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

'''
这里使用的是qq邮箱
使用SSL的通用配置如下：
接收邮件服务器：pop.qq.com，使用SSL，端口号995
发送邮件服务器：smtp.qq.com，使用SSL，端口号465或587
账户名：您的QQ邮箱账户名（如果您是VIP帐号或Foxmail帐号，账户名需要填写完整的邮件地址）
密码：您的QQ邮箱密码
电子邮件地址：您的QQ邮箱的完整邮件地址
'''
#第三方smtp服务 ：
mail_host = "smtp.qq.com"
mail_user = "913816077@qq.com"
##qq邮箱需要特别生成的授权码才能使用smtp服务
mail_pass = "****"

sender = '913816077@qq.com'
receivers = '913816077@qq.com'


#三个参数，第一个为邮件的文本内容，第二个plian来设置文本的格式，第三个用来设置编码
message = MIMEText('ehco 练习邮件测试','plain','utf-8')
message['From']=formataddr(['ehco',sender])
message['To']=formataddr(['fk',receivers])

subject = "ehco de python 邮件测试"
message['Subject'] = '文件主题  测试测试'
try:
    #初始化smtp对象 注意，其使用了ssl加密技术
    smtpObj = smtplib.SMTP_SSL(mail_host,465)
    #连接远程smtp服务 第二个参数为端口号
    #输出 debug 
    smtpObj.set_debuglevel(1)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,[receivers,],message.as_string())
    print('邮件发送成功')
except:
    print('无法发送邮件')