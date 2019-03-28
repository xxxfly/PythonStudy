#-*-coding:utf-8-*-

from PIL import Image
import hashlib
import time
import math
import os

#比较两个 python 字典类型并输出它们的相似度（用 0～1 的数字表示）
class VectorCompare(object):
    #计算矢量大小
    def magnitude(self,concordance):
        total=0
        for word,count in concordance.items():
            total+=count**2
        return math.sqrt(total)

    #计算矢量之间的 cos 值
    def relation(self,concordance1,concordance2):
        relevance=0
        topvalue=0
        for word,count in concordance1.items():
            if word in concordance2:
                topvalue+=count*concordance2[word]
        return topvalue/(self.magnitude(concordance1)*self.magnitude(concordance2))


#将图片转换为矢量
def buildverctor(im):
    d1={}
    count=0
    for i in im.getdata():
        d1[count]=i
        count+=1
    return d1


iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def main():

    v = VectorCompare()

    imageset=[]

    for letter in iconset:
        for img in os.listdir('iconset/%s/'%(letter)):
            temp=[]
            if img!='Thumbs.db' and img!='.DS_Store':
                temp.append(buildverctor(Image.open('iconset/%s/%s'%(letter,img))))
            imageset.append({letter:temp})

    im=Image.open('examples/t18pvs.gif')

    #将图片转换为  8 位像素模式
    im.convert('P')

    im2=Image.new('P',im.size,255)

    temp={}

    #打印颜色直方图
    # print(im.histogram())
    his=im.histogram()
    #对颜色直方图排序
    values={}

    for i in range(256):
        values[i]=his[i]
    
    #颜色直方图的每一位数字都代表了在图片中含有对应位的颜色的像素的数量
    for j,k in sorted(values.items(),key=lambda x:x[1],reverse=True)[:10]:
        print('%d,%d'%(j,k))

    #颜色直方图的每一位数字都代表了在图片中含有对应位的颜色的像素的数量
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix=im.getpixel((y,x))
            temp[pix]=pix
            if pix == 220 or pix == 227: # these are the numbers to get
                im2.putpixel((y,x),0)

    #展示图片
    #im2.show()

    inletter=False
    foundletter=False
    start=0
    end=0

    letters=[]

    for y in range(im2.size[0]):
        for x in range(im2.size[1]):
            pix=im2.getpixel((y,x))
            if pix!=255:
                inletter=True
        if foundletter==False and inletter==True:
            foundletter=True
            start=y
        if foundletter==True and inletter==False:
            foundletter=False
            end=y
            letters.append((start,end))

        inletter=False
    #得到每个字符开始和结束的列序号
    # print(letters)

    count=0
    for letter in letters:
        md5=hashlib.md5()
        im3=im2.crop((letter[0],0,letter[1],im2.size[1]))

        guess=[]

        for image in imageset:
            for x,y in image.items():
                if len(y) !=0:
                    guess.append((v.relation(y[0],buildverctor(im3)),x))
        guess.sort(reverse=True)
        print('%s'%str(guess[0]))
        # md5.update(('%s%s'%(time.time(),count)).encode('utf-8'))
        # im3.save("./%s.gif"%(md5.hexdigest()))
        count+=1


if __name__ == '__main__':
    main()