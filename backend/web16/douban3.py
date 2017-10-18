import os
import requests
from pyquery import PyQuery as pq


"""
这个爬虫可以爬 10 个页面, 把所有 TOP250 电影都爬出来
并且加入了缓存页面功能
再也不用重复请求了(网络请求很浪费时间)
这样做有两个好处
    1, 增加新内容(比如增加评论人数)的时候不用重复请求网络
    2, 出错的时候有原始数据对照(比如 消失的爱人 没有 quote)
"""


class Model():
    """
    基类, 用来显示类的信息
    """
    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Movie(Model):
    """
    存储电影信息
    """
    def __init__(self):
        self.name = ''
        self.score = 0
        self.quote = ''
        self.cover_url = ''
        self.ranking = 0


def cached_url(url):
    """
    缓存, 避免重复下载网页浪费时间
    """
    folder = 'cached'
    filename = url.split('=', 1)[-1] + '.html'
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
            return s
    else:
        # 建立 cached 文件夹
        if not os.path.exists(folder):
            os.makedirs(folder)
        # 发送网络请求, 把结果写入到文件夹中
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
    return r.content


def movie_from_div(div):
    """
    从一个 div 里面获取到一个电影信息
    """
    e = pq(div)

    # 小作用域变量用单字符
    m = Movie()
    m.name = e('.title').text()
    m.score = e('.rating_num').text()
    m.quote = e('.inq').text()
    m.cover_url = e('img').attr('src')
    m.ranking = e('.pic').find('em').text()
    return m


def movies_from_url(url):
    """
    从 url 中下载网页并解析出页面内所有的电影
    """
    page = cached_url(url)
    e = pq(page)
    items = e('.item')
    # 调用 movie_from_div 
    movies = [movie_from_div(i) for i in items]
    return movies


def main():
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}'.format(i)
        movies = movies_from_url(url)
        print('top250 movies', movies)


if __name__ == '__main__':
    main()
