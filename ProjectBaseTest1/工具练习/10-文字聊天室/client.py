#-*-coding:utf-8-*-

import wx
import telnetlib
from time import sleep
import _thread as thread
import random
import re

class LoginFrame(wx.Frame):
    """
    登录窗口
    """

    def __init__(self,parent,id,title,size):
        #初始化，添加控件并绑定事件
        wx.Frame.__init__(self,parent,id,title)
        self.SetSize(size)
        self.Center()
        self.serverAddressLable=wx.StaticText(self,label="Server Address",pos=(10,50),size=(120,25))
        self.userNameLabel=wx.StaticText(self,label="UserName",pos=(40,100),size=(120,25))
        self.serverAddress=wx.TextCtrl(self,pos=(120,47),size=(150,25))
        self.userName=wx.TextCtrl(self,pos=(120,97),size=(150,25))
        self.loginButton=wx.Button(self,label="Login",pos=(80,145),size=(130,30))
        #绑定登录方法
        self.loginButton.Bind(wx.EVT_BUTTON,self.login)
        self.Show()
    
    def login(self,event):
        #处理登录
        try:
            serverAddress=self.serverAddress.GetLineText(0).split(':')
            address=serverAddress[0]            
            port=serverAddress[1]
            con.open(address,port=int(port),timeout=10) 

            response=con.read_some()
            if  response!=b'Connect Success':
                self.showDialog('Error','Connect Fail',(200,100))
                return
            con.write(('login '+str(self.userName.GetLineText(0))+'\n').encode('utf-8'))
            response=con.read_some()
            if response==b'UserName Empty':
                self.showDialog('Error','UserName Empty!',(200,100))
            elif response==b'UserName Empty':
                self.showDialog('Error','UserName Exists!',(200,100))
            else:
                self.Close()
                ChatFrame(None,2,title='Chat Client',size=(500,400))

        except Exception as ex:
            print(str(ex))
            self.showDialog('Error','Connect Fail!',(95,20))

    def showDialog(self,title,content,size):
        #显示错误信息对话框
        print('Error:'+content)
        dialog=wx.Dialog(self,title=title,size=size)
        dialog.Center()
        wx.StaticText(dialog,label=content)
        dialog.ShowModal()


class ChatFrame(wx.Frame):
    """
    聊天窗口
    """
    def __init__(self,parent,id,title,size):
        #初始化，添加控件并绑定事件
        wx.Frame.__init__(self,parent,id,title)
        self.SetSize(size)
        self.Center()

        self.chatFrame=wx.TextCtrl(self,pos=(5,5),size=(490,310),style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.message = wx.TextCtrl(self, pos=(5, 320), size=(300, 25))
        self.sendButton=wx.Button(self,label='Send',pos=(310,320),size=(58,25))
        self.usersButton=wx.Button(self,label='Users',pos=(373,320),size=(58,25))
        self.closeButton=wx.Button(self,label='Close',pos=(436,320),size=(58,25))


        #发送按钮绑定发送消息的方法
        self.sendButton.Bind(wx.EVT_BUTTON,self.send)
        #Users按钮绑定获取在线用户数量的方法
        self.usersButton.Bind(wx.EVT_BUTTON,self.lookUsers)
        #关闭按钮绑定关闭方法
        self.closeButton.Bind(wx.EVT_BUTTON,self.close)
        
        thread.start_new_thread(self.receive,())
        self.Show()

    def send(self,event):
        #发送消息
        message=str(self.message.GetLineText(0)).strip()
        if message!='':
            con.write(('say '+message+'\n').encode('utf-8'))
            self.message.Clear()
        
    def lookUsers(self,event):
        #查看当前在线用户
        con.write(b'look\n')

    def close(self,event):
        #关闭窗口
        con.write(b'logout\n')
        con.close()
        self.Close()
    
    def receive(self):
        #接收服务器的消息
        while True:
            sleep(0.6)
            result=con.read_very_eager()
            if result!='':
                self.chatFrame.AppendText(result)

numChar='0123456789'
enChar='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def getRandom(length=8):
    """
    获取随机码
    @param {int} length 默认为8
    @return {str} 随机码
    """
    if  length<4:
        return None
    
    randomDigit=''
    numCount=random.randint(1,length-1) #数字出现的数量
    enNumber=length-numCount

    for i in range(length):
        #随机添加数字或字母
        if bool(random.randint(0,1)): 
            randomDigit+=random.choice(numChar)
            numCount-=1
        else:
            randomDigit+=random.choice(enChar)
            enNumber-=1

    return randomDigit



if __name__ == '__main__':
    app=wx.App()
    con=telnetlib.Telnet()
    LoginFrame(None,-1,title='Login',size=(320,250))
    app.MainLoop()

    # with open('内蒙电信红包随机码.txt', 'w',encoding='utf-8') as f:
    #     accTup=({'sum':100,'number':30},{'sum':30,'number':150},{'sum':5,'number':2500})
    #     charList=[]
    #     for i in range(3000):            
    #         while True:
    #             char=getRandom(8)
    #             if char in charList:
    #                 continue
    #             else:
    #                 charList.append(char)
    #                 break;
        
    #     for item in accTup:
    #         charCurList=charList[0:item['number']]
    #         for char in charCurList:
    #             line=char+'\t'+str(item['sum'])+'\n'
    #             f.write(line)
                
    #         charList=charList[item['number']:]
        
    #     for char in charList:
    #         line=char+'\t'+'预留'+'\n'
    #         f.write(line)
        