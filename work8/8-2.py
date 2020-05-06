# 2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
import threading
from concurrent.futures import ThreadPoolExecutor
import requests

def getHtmlText(url):#判断URL能否访问 能访问返回True 否则返回False
    print('%s' %(threading.current_thread().name),end='')
    try:
        r=requests.get(url,timeout=2)
        r.raise_for_status()
        print('%s:True' %(url))
        return True
    except:
        print('%s:False' %(url))
        return False

def main():
    try:
        f=open('url_data.txt','r')
        pool=ThreadPoolExecutor(max_workers=5)
        for line in f:
            line=line.strip('\n')
            pool.submit(getHtmlText,line)
        pool.shutdown()
        f.close()
    except:
        print('未找到文件')

main()
    