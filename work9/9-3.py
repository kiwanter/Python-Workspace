# 3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
from socket import *
from multiprocessing import Process
import sys

def send():
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    dest_addr=('127.0.0.1',8888)
    while True:
        send_data=input('输入信息：')
        udp_socket.sendto(send_data.encode('gbk'),dest_addr)
        if send_data == 'exit':
            udp_socket.close()
            sys.exit(0)

def recieve():
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    local_addr=('',8888)
    udp_socket.bind(local_addr)
    while True:
        recv_data=udp_socket.recvfrom(1024)
        data=recv_data[0].decode('gbk')
        if data == 'exit':
            udp_socket.close()
            sys.exit(0)
        print(data)


def main():
    R=Process(target=recieve)
    R.start()
    send()

if __name__ == '__main__':
    main()
    