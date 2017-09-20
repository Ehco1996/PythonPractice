import logging
import pymysql.cursors
import telegram
from telegram.ext import CommandHandler, Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# 注册updater
updater = Updater(token='token')
dispatcher = updater.dispatcher

# 获取邀请码得函数
def get_invite_code():
    con = pymysql.connect(
        host='host',
        user='user',
        password='1pass',
        db='dbname',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    try:
        with con.cursor() as cursor:
            sql = "select code from shadowsocks_invitecode;"
            cursor.execute(sql)
            # 获取一个结果
            result = cursor.fetchone()
    finally:
        con.close()

    # 增加一个简单的判断
    if result:
        invite_code = result['code']
    else:
        invite_code = '当前邀请码已经彻底用完，请在后台联系我'

    print(invite_code)
    return invite_code


# start命令 部分
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="我是一只萌新bot，目前只能发自动发邀请码给大家 其他得我什么都不会..")


# invitecde 命令部分
def invitecde(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=get_invite_code())


# 注册事件处理handler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
invitecode_handler = CommandHandler('invitecode', invitecde)
dispatcher.add_handler(invitecode_handler)

# 开始轮询
updater.start_polling()
