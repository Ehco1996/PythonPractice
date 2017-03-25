#获取昨天的日期 （日期格式的量也是能够想加减的）
import datetime

def getyesterday():
    today = datetime.date.today()
    one = datetime.timedelta(1)
    yesterday = today - one
    return yesterday

print(getyesterday())