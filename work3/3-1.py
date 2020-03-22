import sys
line=[]
while True:
    c=input()
    if not c:
        try:
            f=open('E://test.txt','w')
            for x in line:
                f.write(x)
                f.write('\n')
            f.close()
        except IOError:
            print("error")
        sys.exit(0)
    line.append(c)

