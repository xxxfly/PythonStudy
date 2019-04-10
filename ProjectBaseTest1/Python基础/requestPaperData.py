# -*- coding: utf-8 -*-
import time
import re
import random
import requests

if __name__ == '__main__':
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    depth = 602
    start_url = "http://search.cnki.net/search.aspx?q=abstract%3a%E6%99%AF%E8%A7%82%E7%94%9F%E6%80%81&rank=relevant&cluster=zyk&val=CJFDTOTAL"
    for i in range(depth):
        try:
            url = start_url + "&p=" + str(15*i)

            response = requests.get(url,headers=headers)
            # print(response.text)
            reStr1 = r'<divclass="wz_tab">(.*?)</div>'
            articleList = re.findall(reStr1,response.text.replace('\r\n','').replace('\t','').replace(' ','').replace('&nbsp;',''),re.S|re.M)
            reStr2 = r'<divclass="wz_content"><h3><ahref="(.*?)"target="_blank">.*?</a><ahref=".*?year=201[3-8]'
            with open('url_results.txt', 'a+') as f:
                for art in articleList:
                    url_list = re.findall(reStr2, art)
                    for url in url_list:
                        f.write(url+'\n')
            f.close()
            print("爬取第" + str(i) + "页成功！")
            time.sleep(random.randint(1,3))
        except:
            print("爬取第"+str(i)+"页失败！")
            continue