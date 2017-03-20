# example to use wordcloud to build word pictures
from os import path
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS

# tft pic txt path
txt_path = '/Users/ehco/Documents/example.txt'
cn_font = '/Users/ehco/Documents/hz.ttc'
pic_path = '/Users/ehco/Documents/bk.png'

# read the woole text.
text = open(txt_path).read()

# read the mask image
qbs_mask = np.array(Image.open(pic_path))

stopwords = set(STOPWORDS)
stopwords.add("停止")
# generate a word image
wc = WordCloud(background_color='white', mask=qbs_mask, stopwords=stopwords,
               font_path=cn_font, min_font_size=15).generate(text)


# display the generated image:
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.figure()
plt.imshow(qbs_mask, interpolation='bilinear')
plt.axis('off')
plt.show()
