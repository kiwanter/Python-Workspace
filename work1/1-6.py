a,b=0,1
c=[a,b]
for i in range(10):
    a,b=b,a+b
    c.append(b)
print(c)