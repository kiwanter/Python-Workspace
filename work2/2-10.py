def caclute(a,b,c):
    a=int(a)
    c=int(c)
    if b=='+' :return a+c
    elif b=='-' :return a-c
    elif b=='*' :return a*c
    elif b=='/' :return a/c

a=input('数：')
b=input('运算:')
c=input('数：')
print(a,b,c,'=',caclute(a,b,c))