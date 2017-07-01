'''
挖掘新闻的标题，
并利用结巴分词和词云制作成词云图片
'''


import re
import time
from os import path

import jieba
import jieba.posseg as pseg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from scipy.misc import imread
from wordcloud import WordCloud


def fetch_sina_news():
    '''
    抓取新浪新闻科技类的滚动新闻标题
    返回新闻标题的名字
    '''
    title = []
    url = 'http://roll.news.sina.com.cn/'
    html = requests.get(url)
    html.encoding = 'gb2312'

    soup = BeautifulSoup(html.text, 'lxml')

    news = soup.find_all('span', class_='c_tit')
    for tit in news:
        title.append(tit.text)
    return title


def extract_words(titles):
    '''
    从获取的标题中分词中文词语，
    并返回一个列表
    '''
    words_list = []
    for tit in titles:
        words = jieba.cut(tit)
        for word in words:
            if word not in words_list:
                words_list.append(word)
                words_list.append(' ')

    return words_list


news_titles = fetch_sina_news()
titles = extract_words(news_titles)
content = ''.join(titles)
print(content)



wordcloud = WordCloud(background_color='white',
                      font_path='cn.ttf',max_font_size=40).generate(content)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('xinwen.jpg')
plt.close()