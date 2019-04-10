 #-*- coding: utf-8 -*-

#定义全局变量 数组用来存储名片信息
card_infos=[]

#新增一个名片
def add_new_card_info():
    '''完成新增一个名片'''
    new_name=input("请输入新的名字:")
    new_qq=input("请输入新的QQ:")
    new_weixin=input("请输入新的微信:")
    new_addr=input("请输入新的住址:")

    #定义一个字典，用来存储一个新的名片
    new_info={}
    new_info['name']=new_name
    new_info['qq']=new_qq
    new_info['weixin']=new_weixin
    new_info['addr']=new_addr

    #讲一个字典添加到列表中
    global card_infos
    card_infos.append(new_info)

#删除名片信息
def remove_card_info():
    '''删除名片信息'''
    remove_name=input('请输入要删除的姓名:')
    remove_falg=False #删除的标识
    for temp in card_infos:
        if(temp['name']==remove_name):
            card_infos.remove(temp)
            remove_falg=True
            print('成功删除%s'%remove_name)
            break
    if not remove_falg:
        print('查不此人')

#修改名片信息
def update_card_info():
    '''修改名片信息'''
    update_name=input('请输入要修改的姓名:')
    new_name=input('请输入修改后的姓名:')
    update_flag=False #修改成功的标识，默认不成功
    for i in range(len(card_infos)):
        if card_infos[i]['name']==update_name:
            card_infos[i]['name']=new_name
            update_flag=True
            print('修改成功')
            break
    if not update_flag:
        print('查无此人')
    
#查找名片信息
def find_card_info():
    '''查找名片信息'''
    find_name=input('请输入要查找的姓名：')
    find_flag=False #找到的标识，默认没有找到
    for temp in card_infos:
        if temp['name']==find_name:
            print('%s找到了'%find_name)
            print('%s\t%s\t%s\t%s'%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
            find_flag=True
            break
    if not find_flag:
        print('查无此人')
    

#展示名片信息
def show_all_info():
    '''展示所有名片信息'''
    print('姓名\tQQ\t微信\t地址\t')
    for temp in card_infos:
        print('%s\t%s\t%s\t%s'%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))


def save_2_file():
    '''把已经添加的名片信息保存在文件中'''
    f=open('card_backup.data','w',encoding='utf-8')
    f.write(str(card_infos))
    f.close()

def load_file():
    global card_infos
    try:
        f=open('card_backup.data',encoding='utf-8')
        card_infos=eval(f.read())        
    except Exception:
        pass
    finally:
        f.close()
    
#打印功能菜单
def print_menu():
    '''打印功能菜单'''
    print('*'*50)
    print("名片管理系统 v1.0")
    print("1.添加一个新名片")
    print("2.修改一个名片")
    print("3.删除一个名片")
    print("4.查找一个名片")
    print("5.查看所有名片")
    print("6.存入文件")
    print("7.退出")
    print('*'*50)

def main():
    '''完成对整个程序的控制'''
    #将文件数据加载到程序中
    load_file()
    #1.打印菜单
    print_menu()
    while True:
        #2.获取用户的输入
        num=int(input('请输入操作序号:'))
        #3.根据用户的数据执行相应的功能
        if num==1:
            add_new_card_info()
        elif num==2:
            remove_card_info()
        elif num==3:
            update_card_info()
        elif num==4:
            find_card_info()
        elif num==5:
            show_all_info()
        elif num==6:
            save_2_file()
        elif num==7:
            print("再见")
            break
        else:
            print('输入有误，请重新输入')
        print('')


if __name__ == '__main__':
    main()