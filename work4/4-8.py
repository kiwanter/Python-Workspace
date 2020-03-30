import random
def creatip():
    f=open('ip.txt','w')
    ips=['175.25.254.'+str(x) for x in range(1,255)]
    for i in range(1200):
        f.write(random.sample(ips,1)[0]+'\n')
    f.close()
def tenip():
    f=open('ip.txt','r')
    ipdict=dict()
    for i in f:
        if i in ipdict:
            ipdict[i]+=1
        else:
            ipdict[i]=1
    print(sorted(ipdict.items(),key=lambda d:d[1],reverse=True)[:10])
    f.close()   
creatip()
tenip()