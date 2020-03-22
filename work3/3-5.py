with open('E://Blowing in the wind.txt','r+') as f:
    f.seek(0,0)
    f.write('Blow in the wind\n')
    f.write('Bob Dylan\n')
    f.seek(0,2)
    f.write('\n1962 by Warner Bros.inc')
    f.seek(0,0)
    for i in f.readlines():
        print(i,end='')