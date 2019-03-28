#-*-coding:utf-8-*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from  pyecharts import Geo,Style,Line,Bar,Overlap
from wordcloud import WordCloud,ImageColorGenerator
from os import path
from pylab import mpl
import jieba

#数据清洗
def dataClean():
    f=open(r'月饼数据.txt',encoding='utf-8')
    df=pd.read_csv(f,sep=',',names=['title','price','sales','location'])

    print(df.describe())

    f.close()
    

#文字云图显示
def wordcloudShow():
    
    """对标题进行文字云图分析"""
    f=open(r'月饼数据.txt',encoding='utf-8')
    df=pd.read_csv(f,sep=',',names=['title','price','sales','location'])

    title=df.title.values.tolist() #返回标题的值列表
    #print(title)

    #对每个标题进行分词
    title_s=[]
    for line in title:
        title_cut=jieba.lcut(line) #将标题分解成包含一个个词组的列表
        title_s.append(title_cut)
    
    title_clean=[]
    #停用词表
    stopwords=["月饼","礼品","口味","礼盒","包邮","【","】","送礼","大","中秋节","中秋月饼","2","饼","蓉","多","个","味","斤","送"," ","老","北京","云南","网红老"]

    #剔除停用词表
    for line in title_s:
        line_clean=[]
        for word in line:
            if word not in stopwords:
                line_clean.append(word)
        title_clean.append(line_clean)

    title_clean_dist=[]
    #进行去重
    for line in title_clean:
        line_dist=[]
        for word in line:
            if word not in line_dist:
                line_dist.append(word)
        title_clean_dist.append(line_dist)
    

    allwords_clean_dist=[]
    for line in title_clean_dist:
        for word in line:
            allwords_clean_dist.append(word)
    
    df_allwords_clean_dist=pd.DataFrame({'allwords':allwords_clean_dist})
    
    #对过滤_去重的词语进行汇总统计
    word_count=df_allwords_clean_dist.allwords.value_counts().reset_index()
    word_count.cloumns=['word','count']

    background_Image=plt.imread('1.jpg')

    wc=WordCloud(width=1024,height=768,background_color='white',mask=background_Image,font_path='simhei.ttf\simhei.ttf',max_font_size=400,random_state=50)

    wc=wc.fit_words({x[0]:x[1] for x in word_count.head(100).values})

    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

    d=path.dirname(__file__)

    wc.to_file(path.join(d,'yuebing.jpg'))

def barKeyWordsShow():
    """月饼关键词销量分析"""
    f=open(r'月饼数据.txt',encoding='utf-8')
    df=pd.read_csv(f,sep=',',names=['title','price','sales','location'])

    title=df.title.values.tolist() #返回标题的值列表
    #print(title)

    #对每个标题进行分词
    title_s=[]
    for line in title:
        title_cut=jieba.lcut(line) #将标题分解成包含一个个词组的列表
        title_s.append(title_cut)
    
    title_clean=[]
    #停用词表
    stopwords=["月饼","礼品","口味","礼盒","包邮","【","】","送礼","大","中秋节","中秋月饼","2","饼","蓉","多","个","味","斤","送"," ","老","北京","云南","网红老"]

    #剔除停用词表
    for line in title_s:
        line_clean=[]
        for word in line:
            if word not in stopwords:
                line_clean.append(word)
        title_clean.append(line_clean)

    title_clean_dist=[]
    #进行去重
    for line in title_clean:
        line_dist=[]
        for word in line:
            if word not in line_dist:
                line_dist.append(word)
        title_clean_dist.append(line_dist)
    

    allwords_clean_dist=[]
    for line in title_clean_dist:
        for word in line:
            allwords_clean_dist.append(word)
    
    df_allwords_clean_dist=pd.DataFrame({'allwords':allwords_clean_dist})
    
    #对过滤_去重的词语进行汇总统计
    word_count=df_allwords_clean_dist.allwords.value_counts().reset_index()
    word_count.columns=['word','count']

    w_s_sum = []

    for w in word_count.word:
        i = 0
        s_list = []
        for t in title_clean_dist:
            if w in t:
                s_list.append(int(df.sales[i]))
            i+= 1
        w_s_sum.append(sum(s_list))

    df_w_s_sum=pd.DataFrame({'w_s_sum':w_s_sum})
    df_word_sum=pd.concat([word_count,df_w_s_sum],axis=1,ignore_index=True)
    df_word_sum.columns=['word','count','w_s_sum']
    df_word_sum.sort_values('w_s_sum',inplace=True,ascending=True)
    df_w_s=df_word_sum.tail(30)

    attr=df_w_s['word']
    v1=df_w_s['w_s_sum']

    bar=Bar('月饼关键词销量分布图')

    bar.add('关键词',attr,v1,is_stack=True,xaxis_rotate=30,yaxis_mim=4.2,xaxis_interval=0,is_splitiline_show=False)

    overlap=Overlap()
    overlap.add(bar)
    overlap.render('月饼关键词——销量分布图.html')


#价格区间&月饼数量分布
def barPriceRangeShow():
    """
    价格区间&月饼数量分布
    """
    f=open(r'月饼数据.txt',encoding='utf-8')
    df=pd.read_csv(f,sep=',',names=['title','price','sales','location'])

    #print(df.sort_values(by='price'))
    price_info=df[['price','location']]

    bins= [0,10,50,100,150,200,300,500,1000,5000,8000]
    level= ['0-10','10-50', '50-100','100-150' ,'150-200', '200-500','500-1000','1000-5000','5000-8000','8000以上']

    price_stage=pd.cut(price_info['price'],bins=bins,labels=level).value_counts().sort_index()

    attr=price_stage.index
    print(attr)
    v1=price_stage.values
    print(v1)

    bar=Bar('价格区间&月饼种类数量分布')
    bar.add("",attr,v1,is_stack=True,xaxis_rotate=30,yaxis_min=4.2,xaxis_interval=0,is_splitline_show=False)

    overlap=Overlap()
    overlap.add(bar)
    overlap.render('价格区间&月饼种类数量分布.html')

if __name__ == '__main__':
    pass
    # wordcloudShow()
    # barKeyWordsShow()
    #barPriceRangeShow()
