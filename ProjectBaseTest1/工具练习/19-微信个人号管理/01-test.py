#-*-coding=utf-8-*-

from wxpy import *

if __name__=='__main__':
    # 初始化机器人，扫码登录
    bot=Bot()

    my_friend=bot.friends().search('张雪')[0]

    print(my_friend)

    my_friend.send('Hello 测试测试!')