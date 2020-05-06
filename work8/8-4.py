# 4 多进程通讯：
#   编写一个简单的聊天程序；其中4 多进程通讯：
from multiprocessing import Process,Queue
import os
import sys
import time


# def send():
#     while True:
#         message=input('输入内容(stop结束)：')
#         if message == 'stop':
#             sys.exit(0)
#         print('%s:%s' %(os.getpid,message))
#         time.sleep(1)

def recieve(q):
    while True:
        if q.empty():
            time.sleep(1)
        else:
            message=q.get()
            if message == 'stop':
                sys.exit(0)
            print('\nrecieve:%s' %(message))
if __name__ == '__main__':
    print('聊天室启动')
    q=Queue(maxsize=10)
    p=Process(target=recieve,args=(q,))
    p.start()
    while True:
        message=input('输入内容(stop结束)：')
        q.put(message)
        if message == 'stop':
            sys.exit(0)
        print('send:%s' %(message))
        
    
    