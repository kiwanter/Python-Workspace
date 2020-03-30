import os
import time
for i in os.listdir():
    if os.path.isdir(i):
        print('%-10s' % i,end='')
        print(time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(os.path.getmtime(i))))
    if os.path.isfile(i):
        print('%-10s' % i,end='')
        print(time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(os.path.getmtime(i))),end='')
        print(str(os.path.getsize(i))+'B')