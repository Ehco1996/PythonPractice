import time

from PIL import Image, ImageSequence


ASCII_CHAR = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,^`'.")


def rgb_to_ascii(r, g, b, alpha=256):
    '''
    通过灰度值的映射
    将没一个rgb值对应成一个ascii符
    也就实现了rgb -> ascii
    '''
    # 当像素透明时，直接返回一个空白字符串
    if alpha == 0:
        return ' '

    length = len(ASCII_CHAR)
    gray = int(0.299 * r + 0.587 * g + 0.114 * b)
    # 灰度值和字符串的对应关系
    # 每个字符串对应灰度值的区间是
    unit = (256.0 + 1)/length
    # 找到灰度值所对应字符串的下标
    index = int(gray/unit)
    return ASCII_CHAR[index]


def resize_img(image):
    '''图片以3：5的比例缩小'''
    width, height = image.size
    new_image = image.resize((int(width/6), int(height/10)))
    return new_image


def image_to_ascii_chart(image):
    '''
    # 图片转ascii图
    先来说下实现原理：

    # RGB
    RGB色彩模式是通过对红(R)、绿(G)、蓝(B)
    三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色
    通常情况下，RGB各有256级亮度 其区间为[0,255] 也就是256个阶梯

    # 灰度图
    灰度图是指只含亮度信息，不含色彩信息的图象，
    就象我们平时看到的黑白照片：亮度由暗到明，变化是连续的。

    rgb向灰度值转换的公式是:
    gray = 0.299r + 0.587g + 0.114b
    所以灰度值的区间是 [0,(0.299+0.587+0.114)*255] ~> [0,255]
    '''

    width, height = image.size
    text = ''
    for y in range(height):
        line = ''
        for x in range(width):
            # 找到对应位置的像素点
            dot = image.getpixel((x, y))
            line += rgb_to_ascii(*dot)
        text += line
        text += '\n'
    return text


def gif_to_ascii_chart(path):
    frames = list()
    gif = Image.open(path)
    imgs = [frame.copy() for frame in ImageSequence.Iterator(gif)]
    for img in imgs:
        image = img.convert("RGBA")
        frames.append(image_to_ascii_chart(resize_img(image)))
    return frames


def clear_screen():
    '''
    ANSI 屏幕控制
    '\033[2J' 代表清空屏幕
    '''
    print('\033[2J')


def print_ascii(char_list, times=10):
    for i in range(times):
        for frame in char_list:
            clear_screen()
            print(frame)
            time.sleep(0.1)


def main():
    path = "/Users/ehco/Desktop/5.gif"
    chars = gif_to_ascii_chart(path)
    print_ascii(chars)


if __name__ == '__main__':
    main()
