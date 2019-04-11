# coding=utf-8
# 导入re 模块
import re


def test1():
    pattern='python'
    str1='python-java'
    result=re.match(pattern,str1)
    print(dir(result)) # result object 的属性和方法
    print(result.group()) # 返回匹配的内容

# 字符匹配
def test2():
    """
    字符匹配，从左到右匹配，match 看第一位是否匹配，匹配不到就返回None
    . 匹配的是任意字符
    [] 匹配 [] 中列举的字符 [357] 匹配3 5 7 任意一个都可以，[a-z]代表范围
    \d 匹配数字（digit） \d==[0-9]
    \D 匹配非数字 \D==[^0-9]
    \s 匹配空白，即 空格，tab键...没有显示任何有意义字符的地方
    \S 匹配非空白
    \w 匹配单词字符 即 a-z A-Z 0-9 _  \w==[a-zA-Z0-9_]
    \W 匹配非单词
    """
    print('.'+'-'*20)
    print(re.match('.','i'))
    print(re.match('.','abcds'))
    print(re.match('...','ab'))
    print(re.match('...','abcds'))

    print('[]'+'-'*20)
    print(re.match('1[3579]','13'))
    print(re.match('1[3579]','17'))
    print(re.match('1[3579]','18'))
    print(re.match('1[a-z]','1s'))
    print(re.match('1[a-z]','1d'))
    print(re.match('1[^a-z]','1d'))

    print('\d \D'+'-'*20)
    print(re.match('\d','1'))
    print(re.match('\d','123'))
    print(re.match('\d','ab'))
    print(re.match('\d','1a'))
    print(re.match('\D','12'))
    print(re.match('\D','1s'))
    print(re.match('\D','s1'))
    print(re.match('\D','a'))

    print('\s \S'+'-'*20)
    print(re.match('\s',' '))
    print(re.match('\s',' abc'))
    print(re.match('\s','   '))
    print(re.match('\s','\r\n'))
    print(re.match('\S','ab'))
    print(re.match('\S',' abs'))
    print(re.match('\S','a b'))

    print('\w \W'+'-'*20)
    print(re.match('\w','1'))
    print(re.match('\w','a'))
    print(re.match('\w','1a'))
    print(re.match('\w','_1a'))
    print(re.match('\w','*ab'))
    print(re.match('\w','@qq'))
    print(re.match('\W','1a'))
    print(re.match('\W','@1a'))
    print(re.match('\w\W','1a'))

# 表示数量
def test3():
    """
    表示数量
    * 匹配前一个字符出现 0 次 或者 无数次，即可有可无
    + 匹配前一个字符出现 1 次 或者 无数次，即最少 1 次
    ? 匹配前一个字符出现 1 次 或者 0 次，即要么 1 次，要么没有
    {m} 匹配前一个字符出现 m 次
    {m.} 匹配前一个字符至少出现 m 次
    {m,n} 匹配前一个字符出现 m 到 n 次
    r  raw 原始字符串，可以忽略转义的地方
    """
    print('* '+'-'*20)
    print(re.match('\d*',''))
    print(re.match('\d*','a')) # "a"=="""a"
    print(re.match('\d*','abc'))
    print(re.match('\d*','123'))
    print(re.match('\d*','111'))

    print("+"+"-"*20)
    print(re.match('\d+','123a'))
    print(re.match('\d+','1a'))
    print(re.match('\d+','ab1'))

    print("?"+"-"*20)
    print(re.match('\d?','1abc'))
    print(re.match('\d?','abc'))
    print(re.match('\d?','123abc'))

    print("{m}"+"-"*20)
    print(re.match('\d{3}[a-z]','123abc'))
    print(re.match('\d{3}[a-z]','1234abc'))

    print("{m}"+"-"*20)
    print(re.match('\d{3,}[a-z]','123abc'))
    print(re.match('\d{3,}[a-z]','12345abc'))
    print(re.match('\d{5,}[a-z]','123abc'))

    print("{m,n}"+"-"*20)
    print(re.match('\d{0,1}[a-z]','1abc'))
    print(re.match('\d{0,1}[a-z]','abc'))
    print(re.match('\d{0,1}[a-z]','12abc'))

    print('手机号匹配 '+'-'*20)
    print(re.match('1[35678]\d{9}','138123456789'))
    print(re.match('1[35678]\d{9}','138123456'))
    print(re.match('1[35678]\d{9}','138123456789aa'))
    print(re.match('1[35678]\d{9}','238123456789'))
    print(re.match('1[35678]\d{9}','128123456789'))

    print('r-转义字符串'+'-'*20)
    print(re.match('\\\\n\w','\\nabc'))
    print(re.match(r'\\n\w','\\nabc'))


# 表示边界
def test4():
    """
    表示边界
    ^ 匹配字符串开头
    $ 匹配字符串结尾
    \b 匹配一个单词的边界
    \B 匹配非单词边界
    """
    print('^ '+'-'*20)

    print('$ '+'-'*20)
    print(re.match(r'1[35678]\d{9}$','13812345678ab'))

    print('\b '+'-'*20)
    print(re.match(r'^\w+ve\b','hover'))
    print(re.match(r'^\w+\bve\b','hover'))
    print(re.match(r'^\w+\bve\b','ho ve r'))
    print(re.match(r'^\w+\s\bve\b','ho ve r'))
    print(re.match(r'^\w+.*\bve\b','ho ve r'))

    print('\B '+'-'*20)
    print(re.match(r'^.+ve\B','ho ve r'))
    print(re.match(r'^.+ve\B','ho ver'))
    print(re.match(r'^.+\Bve\B','hover'))
    print(re.match(r'^.+\Bve\B','ho ver'))




def main():
    # # 使用　match 匹配字符串
    # result=re.match(正则表达式,要匹配的字符串)

    # ＃ 如果上一步匹配到数据的话，可以用group提取数据
    # result.group()
    test4()

if __name__ == '__main__':
    main()