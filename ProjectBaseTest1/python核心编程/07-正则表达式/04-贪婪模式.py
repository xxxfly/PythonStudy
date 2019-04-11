# coding=utf-8

import re


def test1():
    """
    python 默认贪婪模式
    """
    st1="""
    <div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
    """
    # 贪婪模式匹配到了依然往下匹配，直到下一批匹配开始，< 后面所有的字符串都认为匹配 .+
    # 正则表达式模式中使用到通配字，那它在从左到右的顺序求值时，会尽量“抓取”满足匹配最长字符串，在我们上面的例子里面，“.+”会从字符串的启始处抓取满足模式的最长字符，其中包括我们想得到的第一个整型字段的中的大部分，“\d+”只需一位字符就可以匹配，所以它匹配了数字“4”，而“.+”则匹配了从字符串起始到这个第一位数字4之前的所有字符。
    print(re.sub(r'<.+>',"",st1))

    print(re.sub(r'<\w+>','',st1))
    print(re.sub(r'</?\w+>','',st1))


def test2():
    """
    贪婪模式    匹配到了依然往下匹配，直到下一批匹配开始
    非贪婪则相反，总是尝试匹配尽可能少的字符。
    在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。要求正则匹配的越少越好。
    """

    print(re.match(r'.+(\d+-\d+-\d+-\d+)','This is a number 234-235-22-423'))
    print(re.match(r'.+(\d+-\d+-\d+-\d+)','This is a number 234-235-22-423').group(1))
    print(re.match(r'(.+)(\d+-\d+-\d+-\d+)','This is a number 234-235-22-423').group())

    # 非贪婪模式
    print(re.match(r'(.+?)(\d+-\d+-\d+-\d+)','This is a number 234-235-22-423').groups())

    print(re.match(r'aa(\d+)','aa2343ddd').group(1))
    print(re.match(r'aa(\d+?)','aa2343ddd').group(1))
    print(re.match(r'aa(\d+)ddd','aa2343ddd').group(1))
    print(re.match(r'aa(\d+?)ddd','aa2343ddd').group(1))

def test3():
    st1="""<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">"""

    print(re.search(r'https.+\.jpg',st1).group())
    print(re.search(r'https.+?\.jpg',st1).group())

   
   

def main():
    test3()

if __name__ == '__main__':
    main()