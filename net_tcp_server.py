#!/usr/bin/env python  
# -*- coding:utf8 -*-  
  
import sys  
import importlib
importlib.reload(sys)
import threading  
import socket  
  
class NetServer(object):
    listN=5
    host = '127.0.0.1'
    port=9527
    
    def dealData(self,client, address):
        try:
        #设置超时时间
            #client.settimeout(500)
        #接收数据的大小
            buf = client.recv(1024)
        #将接收到的信息原样的返回到客户端中
            client.send(buf)
            print(buf)
        #超时后显示退出
        except socket.timeout:
            print ('time out')
        #关闭与客户端的连接
        client.close()
        
    def tcpServer(self):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.bind((self.host, self.port))       # 绑定同一个域名下的所有机器  
        sock.listen(self.listN)  
          
        while True:  
            clientSock, address = sock.accept()
            #dealData(clientSock, address)
            t1 = threading.Thread(target=self.dealData, args=(clientSock,address))
            t1.start() 
              
if __name__ == "__main__":  
    netServer = NetServer()  
    netServer.tcpServer()  
