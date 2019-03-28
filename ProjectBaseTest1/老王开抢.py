 #-*- coding: utf-8 -*-

class Person(object):
    """人的类"""
    def __init__(self,name):
        super(Person,self).__init__()
        self.name=name
        self.gun=None
        self.hp=100
    def put_zidan_to_danjia(self,dan_jia_temp,zi_dan_temp):
        """将子弹安装到弹夹里面"""
        #弹夹，保存子弹
        dan_jia_temp.baocun_zidan(zi_dan_temp)
    def put_danjia_to_gun(self,gun_temp,dan_jia_temp):
        """将弹夹安装到枪中"""
        gun_temp.baocun_danjia(dan_jia_temp)
    def pick_gun(self,gun_temp):
        """拿起一把枪"""
        self.gun=gun_temp
    def shoot_someone(self,someone):
        """让枪发射子弹去打敌人"""
        self.gun.fire(someone)
    def diao_xue(self,power):
        """"根据子弹杀伤力 掉多少血"""
        self.hp-=power

    def __str__(self):
        if self.gun:
            return "%s的血量为%d,他有枪 %s"%(self.name,self.hp,self.gun)
        else:
            if self.hp>0:
                return "%s的血量为%d,他没有枪"%(self.name,self.hp)
            else:
                return "%s 已挂"%(self.name)

class Gun(object):
    '''枪的类'''
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name=name #用来记录枪的类型
        self.danjia=None #用来记录弹夹对象的引用
    def baocun_danjia(self,dan_jia_temp):
        """用一个属性来保存弹夹的引用"""
        self.danjia=dan_jia_temp
    def fire(self,someone):
        """枪对某人射击一发子弹"""
        #先从弹夹中取子弹
        zidan_temp= self.danjia.tanchu_zidan()
        #让这个子弹射击敌人
        if zidan_temp:
            #子弹打中敌人
            zidan_temp.dazhong(someone)
        else:
            print('弹夹中没有子弹了')

    def __str__(self):
        if self.danjia:
            return "枪的信息为：%s,%s"%(self.name,self.danjia)    
        else:
            return "枪的信息为：%s,这把枪没有弹夹"%(self.name)    
        

class DanJia(object):
    """弹夹类"""
    def __init__(self,max_num):
        super(DanJia,self).__init__()
        self.max_num=max_num  #用来记录弹夹最大子弹数
        self.zidan_list=[] #用来记录所有的子弹的引用
    def baocun_zidan(self,zi_dan_temp):
        """将这颗子弹保存"""
        self.zidan_list.append(zi_dan_temp)
    def tanchu_zidan(self):
        """弹出最上面的一颗子弹"""
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None
        
    def __str__(self):
        return "弹夹的信息为：%d/%d"%(len(self.zidan_list),self.max_num)

class ZiDan(object):
    """子弹类"""
    def __init__(self,power):
        super(ZiDan,self).__init__()
        self.power=power  #用来记录子弹的威力
    def dazhong(self,someone):
        """子弹打某人，某人会掉血"""
        #某人会掉血(一颗子弹的威力)
        someone.diao_xue(self.power)

def main():
    '''用来控制整个程序的流程'''
    #1.创建一个老王对象
    laowang=Person('laowang')
    #2.创建一个枪对象
    ak47=Gun('AK47')
    #3.创建一个弹夹对象
    dan_jia=DanJia(30)
    #4.创建一些子弹
    for i in range(15):         
        zi_dan=ZiDan(10)
        #6.老王把子弹安装到弹夹中
        laowang.put_zidan_to_danjia(dan_jia,zi_dan)
    print(dan_jia)
    #7.老王把弹夹安装到枪上
    laowang.put_danjia_to_gun(ak47,dan_jia)
    #8.老王拿枪
    laowang.pick_gun(ak47)
    print(ak47)
    print(laowang)
    #5.创建一个敌人
    laosong=Person("laosong")
    #9.老王开抢打敌人
    for i in range(10):
        laowang.shoot_someone(laosong)
        #测试
        print(laowang)
        print(laosong)
                
if __name__ == '__main__':
    main()