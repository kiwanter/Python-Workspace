# 2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
import threading
import requests

def getHtmlText(url):#判断URL能否访问 能访问返回True 否则返回False
    try:
        r=requests.get(url,timeout=2)
        r.raise_for_status()
        return True
    except:
        return False

if getHtmlText('https://www.baiu.com/'):
    print('True')
else:
    print('False')