Python3基础
MyQR库

安装
sudo pip3 install MyQR

引入
from MyQR import myqr


使用
myqr.run('http://www.baidu.com')

参数
参数	含义	详细
words	二维码指向链接	str，输入链接或者句子作为参数
version	边长	int，控制边长，范围是1到40，数字越大边长越大,默认边长是取决于你输入的信息的长度和使用的纠错等级
level	纠错等级	str，控制纠错水平，范围是L、M、Q、H，从左到右依次升高，默认纠错等级为'H'
picture	结合图片	str，将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片
colorized	颜色	bool，使产生的图片由黑白变为彩色的
contrast	对比度	float，调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
brightness	亮度	float，调节图片的亮度，其余用法和取值与 contrast 相同
save_name	输出文件名	str，默认输出文件名是"qrcode.png"
save_dir	存储位置	str，默认存储位置是当前目录


项目地址：https://github.com/sylnsfar/qrcode
二维码原理：https://blog.csdn.net/u012611878/article/details/53167009

MyQR文件结构
qrcode
│   LICENSE.md  
│   README.md    
│   requirements.txt    #环境依赖文件
|   myqr.py
|
└───MyQR
│   │   __init__.py
│   │   myqr.py     #调用的文件
│   │   terminal.py #设置参数
|   |
│   └───mylibs
│       │   __init__.pt
│       │   constan.py  #数据分析
|       |   data.py     #数据编码
│       │   ECC.py      #纠错编码，Error Correction Codewords 
|       |   structure.py    #数据结构
|       |   matrix.py       #获得QR矩阵
|       |   draw.py         #生成二维码
|       |   theqrmodule.py  #结合函数
│   
└───example
    │   0.png
    │   1.png
    |   2.png
    |   ...


生成二维码的步骤
2.1 数据分析MyQR/mylibs/constan.py

确定编码的字符类型，按相应的字符集转换成符号字符。

2.2 数据编码MyQR/mylibs/data.py

将数据字符转换为位流，每8位一个码字，整体构成一个数据的码字序列。

2.3 纠错编码MyQR/mylibs/ECC.py

按需要将上面的码字序列分块，并根据纠错等级和分块的码字，产生纠错码字，并把纠错码字加入到数据码字序列后面，成为一个新的序列。


创建二维码的矩阵
# MyQR/mylibs/matrix.py
def get_qrmatrix(ver, ecl, bits):
    num = (ver - 1) * 4 + 21
    qrmatrix = [[None] * num for i in range(num)]
    # 添加查找器模式和添加分隔符
    add_finder_and_separator(qrmatrix)

    # 添加校准模式
    add_alignment(ver, qrmatrix)

    # 添加时间模式
    add_timing(qrmatrix)

    # 添加涂黑模块和保留区域
    add_dark_and_reserving(ver, qrmatrix)

    maskmatrix = [i[:] for i in qrmatrix]

    # 放置数据位
    place_bits(bits, qrmatrix)

    # 蒙版操作
    mask_num, qrmatrix = mask(maskmatrix, qrmatrix)

    # 格式信息
    add_format_and_version_string(ver, ecl, mask_num, qrmatrix)

    return qrmatrix


生成二维码MyQR/mylibs/draw.py
def draw_qrcode(abspath, qrmatrix):
    unit_len = 3
    x = y = 4*unit_len
    pic = Image.new('1', [(len(qrmatrix)+8)*unit_len]*2, 'white')   #新建一张白色的底图

    '''
    循环矩阵中的单位，在需要涂黑的单位启用dra_a_black_unit()函数涂黑。
    '''
    for line in qrmatrix:
        for module in line:
            if module:
                draw_a_black_unit(pic, x, y, unit_len)  #画出黑单位
            x += unit_len
        x, y = 4*unit_len, y+unit_len

    saving = os.path.join(abspath, 'qrcode.png')
    pic.save(saving)    # 保存二维码图片
    return saving

合并图片的原理
    qr = Image.open(qr_name)    #读取二维码图片
    qr = qr.convert('RGBA') if colorized else qr    #判断二维码是否有色

    bg0 = Image.open(bg_name).convert('RGBA')   #读取要合并的图片
    bg0 = ImageEnhance.Contrast(bg0).enhance(contrast)  # 调节对比度
    bg0 = ImageEnhance.Brightness(bg0).enhance(brightness)  # 调节亮度

将新加的图片覆盖原有的二维码图片，生成新的图片并保存。
    for i in range(qr.size[0]-24):
        for j in range(qr.size[1]-24):
            if not ((i in (18,19,20)) or (j in (18,19,20)) or (i<24 and j<24) or (i<24 and j>qr.size[1]-49) or (i>qr.size[0]-49 and j<24) or ((i,j) in aligs) or (i%3==1 and j%3==1) or (bg0.getpixel((i,j))[3]==0)):
                qr.putpixel((i+12,j+12), bg.getpixel((i,j)))


