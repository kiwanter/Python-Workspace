import sys
T=[]
try:
    f=open('E://test.txt','r')
    while True:
        L=f.readline()
        if not L:
            f.close()
            for i,s in enumerate(T,1):
                print(i,s)
            sys.exit(0)
        L=L.rstrip()
        T.append(L)
except IOError:
    print('error')
