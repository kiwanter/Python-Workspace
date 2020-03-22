f1=open('E://01.txt','r')
f2=open('E://02.txt','r')
a=f1.read()
b=f2.read()
f1.close()
f2.close()
al=a.split(' ')
bl=b.split(' ')
aw={}
bw={}
for i in al:
    if i in aw:
        aw[i]=aw[i]+1
    else:
        aw[i]=1
for i in bl:
    if i in bw:
        bw[i]=bw[i]+1
    else:
        bw[i]=1 
#print(aw)
#print(bw)
at=list(aw.items())
at.sort(key=lambda x:int(x[1]),reverse=True)
at=at[:10]
#print(at)
bt=list(bw.items())
bt.sort(key=lambda x:int(x[1]),reverse=True)
bt=bt[:10]
#print(bt)
count=0
af=[]
for w in at:
    c=w[0]
    af.append(c)
bf=[]
for w in bt:
    c=w[0]
    bf.append(c)
set1=set(af)
set2=set(bf)
print('重复词汇：'+str(set1 & set2))