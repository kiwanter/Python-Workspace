# 1  有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#      B 利用线程池来实现
import threading
import random
def fun():
    for i in range(20):
        print(random.randint(0,100))

f1=threading.Thread(target=fun)
f2=threading.Thread(target=fun)
f3=threading.Thread(target=fun)
f4=threading.Thread(target=fun)
f5=threading.Thread(target=fun)

f1.start()
f2.start()
f3.start()
f4.start()
f5.start()
