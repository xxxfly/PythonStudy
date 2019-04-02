## wxpy: 用 Python 玩微信

### github 地址：https://github.com/youfou/wxpy

### 说明文档：http://wxpy.readthedocs.io
### 安装
wxpy 支持 Python 3.4-3.6，以及 2.7 版本  
将下方命令中的 "pip" 替换为 "pip3" 或 "pip2"，可确保安装到对应的 Python 版本中  
`pip install -U wxpy`
或者  
`pip install -U wxpy -i "https://pypi.doubanio.com/simple/"`


### 使用  

**登录**
```python
# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
```

**找到好友**
```python
# 搜索名称含有 "游否" 的男性深圳好友
my_friend = bot.friends().search('游否', sex=MALE, city="深圳")[0]c
```

**发送消息**
```python
# 发送文本给好友
my_friend.send('Hello WeChat!')
# 发送图片
my_friend.send_image('my_picture.jpg')
```

**自动相应各类消息**
```python
# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')
```

**保持登录**
```python
# 进入 Python 命令行、让程序保持运行
embed()

# 或者仅仅堵塞线程
# bot.join()
```