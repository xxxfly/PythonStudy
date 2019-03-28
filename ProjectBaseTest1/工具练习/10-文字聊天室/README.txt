 

来源: 实验楼
链接: https://www.shiyanlou.com/courses/970
本课程内容，由作者授权实验楼发布，未经允许，禁止转载、下载及非法传播


wxPython 、asynchat、_thread 等模块开发一个图形界面的聊天室程序。


知识点：
    asyncore 、asynchat模块使用
    wxPython 图形开发


由于 Python 是一门带 GIL 的语言，所以在 Python 中使用多线程处理IO操作过多的任务并不是很好的选择。同时聊天服务器将同多个 socket 进行通信，所以我们可以基于 asyncore 模块实现聊天服务器。aysncore 模块是一个异步的 socket 处理器，通过使用该模块将大大简化异步编程的难度。asynchat 模块在 asyncore 模块的基础上做了进一步封装，简化了基于文本协议的通信任务的开发难度。



