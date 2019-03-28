#-*-coding:utf-8-*-

import sys
from PIL import Image
import argparse



#字符画是一系列字符的组合，我们可以把字符看作是比较大块的像素，一个字符能表现一种颜色（暂且这么理解吧），字符的种类越多，可以表现的颜色也越多，图片也会更有层次感。

#灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像


#gray=0.2126*r+0.7152*g+0.0722*b


#画画所需的字符集
ascii_char=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#RGB值转字符的函数
def get_char(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    length=len(ascii_char)
    gray=int(0.2126*r+0.7152*g+0.0722*b)

    unit=(256.0+1)/length
    return ascii_char[int(gray/unit)]


def main():
    #命令行输入参数处理
    parser=argparse.ArgumentParser()

    parser.add_argument('file') #输入文件
    parser.add_argument('-o','--output') #输出文件
    parser.add_argument('--width',type=int,default=80) #输出字符画宽
    parser.add_argument('--height',type=int,default=80) #输出字符画高

    #获取参数
    args=parser.parse_args()

    IMG=args.file
    WIDTH=args.width
    HEIGHT=args.height
    OUTPUT=args.output

    im=Image.open(IMG)
    im=im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt=''


    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt+=get_char(*im.getpixel((j,i)))
        txt+='\n'

    print(txt)

    #字符画输出到指定文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open('output.txt','w') as f:
            f.write(txt)



if __name__ == '__main__':
    main()
