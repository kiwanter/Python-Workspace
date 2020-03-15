import random
a=[]
for i in range(0,random.randint(5,10)):
    k=random.randint(0,99)
    a.append(k)
print(a)
b=[]
for i in range(0,random.randint(5,10)):
    k=random.randint(0,99)
    b.append(k)
c=tuple(b)
print(c)