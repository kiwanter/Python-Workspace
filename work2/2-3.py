#编写一个函数, 传入一个数字列表, 输出列表中的奇数; 数字列表请用随机数函数生成
import random
def odd(a):
    b=[]
    for i in a:
        if(i%2==1):
            b.append(i)
    return b

a=[]
for i in range(random.randint(5,10)):
    a.append(random.randint(1,99))
print(a)
print(odd(a))