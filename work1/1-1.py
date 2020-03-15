odd=[]
even=[]
prime=[]
user1=[]
for i in range(0,50):
    if(i%2==0):
        even.append(i)
        if(i%3)==0:
            user1.append(i)
    if(i%2!=0):
        odd.append(i)
    isprime=1
    for j in range(2,i):
        if(i%j==0):
            isprime=0
    if(i>=2 and isprime==1):
        prime.append(i)
print("偶数：",even)
print("奇数：",odd)
print("质数：",prime)
print("同时被二三整除：",user1)
    