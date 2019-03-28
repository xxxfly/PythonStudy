# -*- coding: UTF-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys,os
import subprocess

class ServerException(Exception):
    '''服务器内部错误'''
    pass


class case_no_file(object):
    '''该路径不存在'''

    def test(self,handler):
        return not os.path.exists(handler.full_path)

    def act(self,handler):
        raise ServerException("'{0}' not found".format(handler.path))

class case_existing_file(object):
    '''该路径是文件'''
    def test(self,handler):
        return  os.path.isfile(handler.full_path)
    
    def act(self,handler):
        handler.handle_file(handler.full_path)


class case_directory_index_file(object):
    '''默认路径'''
    def index_path(self,handler):
        return os.path.join(handler.full_path,'index.html')
    
    #判断目标路径是否是目录&&目录下的是否有 index.html
    def test(self,handler):
        return os.path.isdir(handler.full_path) and \
               os.path.isfile(self.index_path(handler))
    
    #相应index.html 的内容
    def act(self,handler):
        handler.handle_file(self.index_path(handler))

class case_cgi_file(object):
    '''脚本文件处理'''

    def test(self,handler):
        return os.path.isfile(handler.full_path) and \
               handler.full_path.endswith('.py')
            
    def act(self,handler):
        #运行脚本
        handler.run_cgi(handler.full_path)

class case_always_fail(object):
    '''所有情况都不符合时的默认处理类'''
    def test(self,handler):
        return True
    
    def act(self,handler):
        raise ServerException("Unknow object '{0}'".format(handler.path))


class RequestHandler(BaseHTTPRequestHandler):
    """处理请求并返回页面"""

    # 页面模板
    Page = '''\
        <html>
        <body>
        <table>
        <tr>  <td>Header</td>         <td>Value</td>          </tr>
        <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
        <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
        <tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
        <tr>  <td>Command</td>        <td>{command}</td>      </tr>
        <tr>  <td>Path</td>           <td>{path}</td>         </tr>
        </table>
        </body>
        </html>
    '''

    Error_Page="""\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """

    #所有可能的情况
    Cases=[case_no_file(),case_cgi_file(),case_existing_file(),case_directory_index_file(),case_always_fail()]

    # 处理GET请求
    def do_GET(self):
        try:
            #文件完整路径
            self.full_path=os.getcwd()+self.path

            #遍历所有的情况
            for case in self.Cases:
                #如果满足该类条件
                if  case.test(self):
                    #调用相应的act 函数
                    case.act(self)
                    break

        except Exception as ex:
            self.handle_error(ex)
        
    def run_cgi(self,full_path):
        data=subprocess.check_output(["python",full_path],shell=True)
        self.send_content(data)

    def handle_file(self,full_path):
        try:
            with open(full_path,'rb') as reader:
                content=reader.read()
            self.send_content(content)
        except IOError as ex:
            msg="'{0}' connot be read:{1}".format(self.path,ex)
            self.handle_error(msg)
    
    def handle_error(self,msg):
        content=self.Error_Page.format(path=self.path,msg=msg)
        self.send_content(content.encode('utf-8'))

    def create_page(self):
        values = {
            'date_time': self.date_time_string(),
            'client_host': self.client_address[0],
            'client_port': self.client_address[1],
            'command': self.command,
            'path': self.path
        }
        page = self.Page.format(**values)        
        return page

    def send_content(self, page):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(page)))
        self.end_headers()
        # self.wfile.write(page.encode('utf-8'))
        self.wfile.write(page)





def main():
    serverAddress = ('', 8899)
    server = HTTPServer(serverAddress, RequestHandler)
    try:
        print('开启服务器127.0.0.1,端口号:%d' % 8899)
        # 启动服务器
        server.serve_forever()
    except:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
