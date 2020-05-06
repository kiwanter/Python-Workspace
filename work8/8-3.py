# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度

import time
import threading
from concurrent.futures import ThreadPoolExecutor
def prime(i:int):
    if i<=1:
        return False
    elif i<=3:
        return True
    elif i==4:
        return False
    else:
        for j in range(2,int(i/2)):
            if i%j == 0:
                return False
        return True

def outer(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print(end-start)
    return inner()

@outer
def NOthread():
    count=0
    for i in range(1,10000):
        if prime(i):
            print(i,end=' ')
            count+=1
    print('count:%d'%(count))
    print('NOthread:',end='')

@outer
def Fourthread():
    pool=ThreadPoolExecutor(max_workers=4)
    count=0
    for i in range(1,10000):
        future=pool.submit(prime,i)
        if future.result():
            print(i,end=' ')
            count+=1
    print('count:%d'%(count))
    print('Fourthread:',end='')

@outer
def Tenthread():
    pool=ThreadPoolExecutor(max_workers=10)
    count=0
    for i in range(1,10000):
        future=pool.submit(prime,i)
        if future.result():
            print(i,end=' ')
            count+=1
    print('count:%d'%(count))
    print('Tenthread:',end='')
    

NOthread
Fourthread
Tenthread