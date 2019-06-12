# -*- coding: utf-8 -*-

from pymongo import *
import numpy as np
import pandas as pd
from pyecharts.charts import Line,Bar,Grid
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


def cjPriceTrend(sheetname,city):
    '''成交价格趋势'''
    # 获取mongodb 对象
    mongo=MongoDBHelper('127.0.0.1',27017,'spider_data','spider_data','spider_data')
    col=mongo.getCol(sheetname)

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
                "avg_onPrice":{"$avg":"$onPrice"},
                "count":{"$sum":1}
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
    v_count=list(map(lambda x:float('%d'%x),list(p_result['count'])))
    # print(attr)
    print(v_count)

    # 单价
    line_unit=(
        Line(init_opts=opts.InitOpts(width="100%",height="400px"))
        .add_xaxis(attr)
        .add_yaxis('单价',v_unit)
        .set_global_opts(title_opts=opts.TitleOpts(title=city+'单价趋势',pos_left='10%'),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        datazoom_opts=opts.DataZoomOpts(is_show=True,pos_top='44%'))
    
    )

    # 数量
    bar_count=(
        Bar(init_opts=opts.InitOpts(width="100%",height="400px"))
        .add_xaxis(attr)
        .add_yaxis('数量',v_count)
        .set_global_opts(title_opts=opts.TitleOpts(title=city+'成交房屋数量',pos_left='10%',pos_top='54%'),
        legend_opts=opts.LegendOpts(pos_top="54%"))
    )

    grid=(
        Grid(init_opts=opts.InitOpts(width="100%",height='800px'))
        .add(line_unit,grid_opts=opts.GridOpts(pos_bottom="60%"))
        .add(bar_count,grid_opts=opts.GridOpts(pos_top="56%"))
    )
    grid.render('html/01-%s.html'%(city,))

    # 成交价格
    bar_price=(
        Bar(init_opts=opts.InitOpts(width="100%"))
        .add_xaxis(attr)
        .add_yaxis('成交价格/万',v_dealPrice)
         .add_yaxis('挂牌价格/万',v_onPrice)
        .set_global_opts(title_opts=opts.TitleOpts(title=city+'交易均价趋势',pos_right='20%'),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        datazoom_opts=opts.DataZoomOpts(is_show=True))
    )
    bar_price.render('html/02-%s.html'%(city,))


def cjAreaPriceTrend(sheetname,area,city,areaName):
    '''地区成交价格趋势'''
        # 获取mongodb 对象
    mongo=MongoDBHelper('127.0.0.1',27017,'spider_data','spider_data','spider_data')
    col=mongo.getCol(sheetname)

    # 管道参数
    pipe_args=[
        {"$match":{
                "houseArea":area
            }
        },
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

    # 单价
    line1=(
        Line(init_opts=opts.InitOpts(width="100%"))
        .add_xaxis(attr)
        .add_yaxis('单价/元',v_unit)
        .set_global_opts(title_opts=opts.TitleOpts(title=areaName,subtitle=city+'单价趋势',pos_right='20%'),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        datazoom_opts=opts.DataZoomOpts(is_show=True))
    )
    line1.render('html/01-%s-%s.html'%(city,areaName))

    # 成交价格
    line2=(
        Line(init_opts=opts.InitOpts(width="100%"))
        .add_xaxis(attr)
        .add_yaxis('成交价格/万',v_dealPrice)
        .add_yaxis('挂牌价格/万',v_onPrice)
        .set_global_opts(title_opts=opts.TitleOpts(title=areaName,subtitle=city+'交易均价趋势',pos_right='20%'),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        datazoom_opts=opts.DataZoomOpts(is_show=True))
    )
    line2.render('html/02-%s-%s.html'%(city,areaName))

# 二手房代售价格
def esfPriceTrend(sheetname,city):
    pass

if __name__ == '__main__':
    # cjPriceTrend('hzlianjiachengjiao','杭州')
    cjPriceTrend('whlianjiachengjiao','武汉')
    # cjAreaPriceTrend()
    