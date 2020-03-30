import os
def getdirsize(dir):
    size=0
    for i in os.listdir(dir):
        p=dir+'\\'+i
        if os.path.isfile(p):
            size+=os.path.getsize(p)
            print(i,end=' ')
            print(os.path.getsize(p))
        if os.path.isdir(p):
            size+=getdirsize(p)
            print(i,end=' ')
            print(getdirsize(p))
    return size
print(getdirsize('C:\Python\workspace\est'))