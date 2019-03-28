#-*-coging:utf-8-*-

from MyQR import myqr


def test1():
    """普通二维码"""
    myqr.run('http://www.baidu.com')

def test2():
    """生成自定义图片二维码"""
    myqr.run(
        words='http://www.baidu.com',
        picture='Sources/害羞.png',
        save_name='test2.png'
    )

def test3():
    """生成自定义图片加颜色的二维码"""
    myqr.run(
        words='http://www.baidu.com',
        picture='Sources/害羞.png',
        colorized=True,
        save_name='test3.png'
    )

def test4():
    """生成带gif图的二维码"""
    myqr.run(
        words='http://www.baidu.com',
        picture='Sources/gakki.gif',
        colorized=True,
        save_name='test4.gif'
    )

def main():
    #test1()
    # test2()
    # test3()
    test4()

if __name__ == '__main__':
    main()