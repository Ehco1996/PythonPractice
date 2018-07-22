import pymysql.cursors

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