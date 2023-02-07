from socketserver import BaseRequestHandler, TCPServer
import os


class EchoHandler(BaseRequestHandler):
    """服务器响应"""
    def handle(self):
        print('Got connection from', self.client_address)
        # 先清空文件
        with open(f'./received.ps', 'wb') as f:
                f.write(b'')
        # 然后持续接受数据
        while True:
            msg = self.request.recv(8192)
            # 用append模式写到 received.ps 里面
            with open(f'./received.ps', 'ab+') as f:
                f.write(msg)
            # print(msg[:5])
            if not msg:
                # 直到数据接受完成
                print('ps数据接受完成，开始转换成pdf文件')
                # 用ghostscript转换成pdf文件
                os.system('ps2pdf received.ps')
                print("打印完成！")
                # 结束连接
                break

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()