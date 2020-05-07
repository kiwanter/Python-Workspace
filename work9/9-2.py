# 2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出
import socket
def main():

    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    local_addr=('',9999)

    udp_socket.bind(local_addr)

    recv_data = udp_socket.recvfrom(1024) 


    print(recv_data[0].decode('gbk'))
    print(recv_data[1])

    udp_socket.close()

if __name__ == '__main__':
    main()
    