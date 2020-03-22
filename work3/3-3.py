#数据结构 “学号 姓名 分数”
import sys
f=open('E://test.txt','r')
T=list()
while True:
    L=f.readline()
    S=L.split()
    if len(S)==3:
        T.append(S)
    if not L:
        f.close()
        T.sort(key=lambda e:int(e[2]),reverse=True)
        for i in T:
            print(i)
        sys.exit(0)