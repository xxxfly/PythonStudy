# -*- coding: utf-8 -*-

from pymongo import *
import numpy as np
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts



class MongoDBHelper(object):
    """
    MongoDB 类
    """
    def __init__(self,host,port,dbname,username,pwd):
        """
        获得客户端，建立连接
        """
        self.host=host
        self.port =port
        self.dbname = dbname
        self.username=username
        self.pwd=pwd
        
    def mgClient(self):
        """
        创建 MongoDB 数据库连接
        """
        self.client=MongoClient("mongodb://%s:%s@%s:%s/%s"%(self.username,self.pwd,self.host,self.port,self.dbname))

    def getCol(self,collectionName):
        """
        获取表对象
        """ 
        col=None
        try:
            self.mgClient()  
            db=self.client[self.dbname]
            self.collection=db[collectionName]
            col=self.collection
        except Exception as ex:
            print('获取集合出错:'+ex)

        return col


def cjPriceTrend():
    '''成交价格趋势'''
    # 获取mongodb 对象
    mongo=MongoDBHelper('127.0.0.1',27017,'spider_data','spider_data','spider_data')
    col=mongo.getCol('whlianjiachengjiao')

    # 管道参数
    pipe_args=[
        {"$project":{
                "dealPrice":1,
                "onPrice":1,
                "unitPrice":1,
                "month":{"$substr":["$dealDate",0,7]}
            }
        },
        {"$group":{
                "_id":"$month",
                "avg_unit":{"$avg":"$unitPrice"},
                "avg_dealPrice":{"$avg":"$dealPrice"},
                "avg_onPrice":{"$avg":"$onPrice"}
           }
        },
        {"$sort":{
                "_id":1
            }
        }
    ]

    cur_result=col.aggregate(pipeline=pipe_args)
    # for item in cur_result:
    #     print('%s %.2f %.2f %.2f'%(item['_id'],item['avg_unit'],item['avg_dealPrice'],item['avg_onPrice']))

    p_result=pd.DataFrame(list(cur_result))

    attr=list(p_result['_id'])
    v_dealPrice=list(map(lambda x:float('%.2f'%x),list(p_result['avg_dealPrice'])))
    v_onPrice=list(map(lambda x:float('%.2f'%x),list(p_result['avg_onPrice'])))
    v_unit=list(map(lambda x:float('%.2f'%x),list(p_result['avg_unit'])))
    # print(attr)
    # print(v_unit)

    line=(
        Line()
        .add_xaxis(attr[18:])
        .add_yaxis('单价',v_unit[18:])
        .set_global_opts(title_opts=opts.TitleOpts(title='武汉单价趋势'))
    )
    line.render('01.html')

    # line=(
    #     Line()
    #     .add_xaxis(attr[18:])
    #     .add_yaxis('成交价格/万',v_dealPrice[18:])
    #      .add_yaxis('挂牌价格/万',v_onPrice[18:])
    #     .set_global_opts(title_opts=opts.TitleOpts(title='武汉交易均价趋势'))
    # )
    # line.render('02.html')

if __name__ == '__main__':
    cjPriceTrend()
    