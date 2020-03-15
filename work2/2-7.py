import random
dict1={}
for i in range(20):
    dict1[i+1]=random.randint(60,100)
print(dict1)
A,B,C,D={},{},{},{}
for k,V in dict1.items():
    if dict1[k]>=90:A[k]=dict1[k]
    elif dict1[k]>=80:B[k]=dict1[k]
    elif dict1[k]>=70:C[k]=dict1[k]
    else: D[k]=dict1[k]
print('A级：',A)
print('B级：',B)
print('C级：',C)
print('D级：',D)
