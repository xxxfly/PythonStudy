#-*-coding:utf-8-*-

import re

class Templite(object):
    def __init__(self,text,*contexts):
        """'text'是输入的模板
        'contents'是输入的数据与过滤器函数
        """
        self.content={}
        for content in contexts:
            self.content.update(content)


#创建Templite对象
templite=Templite('''
    <h1>hello {{name|upper}}!<h1>
    {% for topic in topics %}
        <p>You are interested in {{topic}}.</p>
    {% endfor %}
    ''',
    {'upper':str.upper}
)

#稍后调用 render 导入数据
text=templite.render({
    'name':'Jane',
    'topics':['Python','Geometry','Juggling']
})


#代码构建器
class CodeBulider(object):
    def __init__(self,indent=0):
        self.code=[]
        self.indent_level=indent

    #自动缩进
    def add_line(self,line):
        self.code.extend([' '*self.indent_level,line,'\n'])

    INDENT_STEP=4 #PEP8 标准4空格缩进

    def indent(self):
        """增加一级缩进"""
        self.indent_level+=self.INDENT_STEP

    def dedent(self):
        """减少一级缩进"""
        self.indent_level-=self.INDENT_STEP
    
    def add_section(self):
        section=CodeBulider(self.indent_level)
        self.code.append(section)
        return section
    
    def __str__(self):
        return "".join(str(c) for c in self.code)

    def get_globals(self):
        """运行代码并返回名字空间字典"""
        #检查缩进，保证所有块（block）都已经处理完
        assert self.indent_level=0
        #得到生成的代码
        python_source=str(self)
        #运行代码后得到的名字空间（变量字典）
        global_namespace={}
        #如果没有 local_namespace 参数，则 global_namespace 会同时包含局部与全局的变量
        exec(python_source,global_namespace)
        return global_namespace


