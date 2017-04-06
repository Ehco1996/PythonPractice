# example to use wordcloud to build word pictures
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud ,ImageColorGenerator



word_str = ''
with open('/Users/ehco/Documents/codestuff/PythonPractice/week6/斗破苍穹_count.txt','r') as f:
    for i in range(600):
        word_str += (f.readline().strip())

print(word_str)

#读取mask
mask = np.array(Image.open('/Users/ehco/Documents/codestuff/PythonPractice/week6/斗破苍穹.png'))

mask_color = ImageColorGenerator(mask)

# generate a word image
wc = WordCloud(font_path='/Users/ehco/Documents/codestuff/PythonPractice/week6/yuppy.ttf',
                mask=mask,background_color='white',min_font_size=10,max_font_size=50,margin=5,scale=1)

wc.generate(word_str)

# display the generated image:
#根据背景图片的颜色 生成词云
plt.imshow(wc.recolor(color_func=mask_color))
plt.axis('off')
plt.show()