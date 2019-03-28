#-*-coding:utf-8-*-

import requests
import re



#下载网页
def get_html_text(url):
    """
    下载网页获取网页内容
    @param url  要下载的网页地址
    """
    try:
        res=requests.get(url,timeout=30)
        res.raise_for_status()
        res.encoding=res.apparent_encoding
        return res.text
    except Exception as ex:
        print('下载网页出错:'+str(ex))
        return ''

#解析网页并保存数据
def parse_page(html):
    """
    解析网页数据
    """
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)  #列表显示价格
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html) #列表显示标题
        loc = re.findall(r'\"item_loc\"\:\".*?\"', html) #列表的地方
        sale = re.findall(r'\"view_sales\"\:\".*?\"', html) #列表显示的付款人数

        print('plt:%s\ttlt:%s\tloc:%s\tsale:%s'%(str(plt),str(tlt),str(loc),str(sale)))
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            title=title.replace('，','')    
            title=title.replace(',','')        
            location=eval(loc[i].split(':')[1])
            location=location.split(' ')[0]
            sales=eval(sale[i].split(':')[1])
            sales=re.match(r'\d+',sales).group(0)
            print(title)
            with open('大闸蟹数据.txt','a',encoding='utf-8') as f:
                f.write(title+','+price+','+sales+','+location+'\n')

    except Exception as identifier:
        print("")

def main():
    goods='大闸蟹'
    depth=1
    start_url='https://s.taobao.com/search?q='+goods
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            print('url:'+url)
            html=get_html_text(url)
            parse_page(html)
        except:
            continue

if __name__ == '__main__':
    main()
