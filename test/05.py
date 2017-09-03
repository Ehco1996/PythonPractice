'''
写程序提取http://www.yhd.com/marketing/allproduct.html 里所有红色字体的商品分类，
并从http://item.yhd.com/item/53938012 获取价格和库存信息（是否在售）
'''

red_url = 'http://www.yhd.com/marketing/allproduct.html'
phone_url = 'http://item.yhd.com/item/53938012'


from bs4 import BeautifulSoup
import requests


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


# 这里不用自定义headers也能获取到数据Í
def parse_red_goods(url):
    '''
    找到红色标签下所有商品的分类和url链接
    '''
    text = get_html(url)
    soup = BeautifulSoup(text, 'lxml')

    cate_list = []
    # 找到左边的分类
    left = soup.find('div', class_='fl')
    content = left.find_all('em')
    for rec in content:
        cate_list.append({
            'name': rec.span.a.text,
            'url': rec.span.a['href'], })

    # 找到右边边的分类
    left = soup.find('div', class_='fr')
    content = left.find_all('em')
    for rec in content:
        cate_list.append({
            'name': rec.span.a.text,
            'url': rec.span.a['href'], })

    return cate_list


phone_ajax_url = 'http://gps.yhd.com/restful/detail?mcsite=1&provinceId=1&cityId=1&countyId=29&pmId=66315636&ruleType=2&businessTagId=16&callback=jQuery1113009611781806779574_1504099571978&_=1504099571979'


def parse_good_info(url):
    '''
    查找iphone6s的价格和库存
    '''
    text = get_html(url)
    # 对信息进行初步格式化 删掉data无用信息
    content = text[text.find('{') + 1:-2]
    data_dict = {}
    # 将所有的类json数据格式化存入字典
    for rec in content.split(','):
        data_dict[rec.split(":")[0].replace(
            '"', '').replace('"', '')] = rec.split(':')[1]

    # 查找我们想要的信息
    price = data_dict['currentPrice']
    stock = data_dict['currentStockNum']

    return '价格：{} 库存{}'.format(price, stock)


print(parse_good_info(phone_ajax_url))
