f=open('log.txt','w')
f.close()
def outer(func):
    def inner(*args):
        f=open('log.txt','a')
        f.write('start %s(%s)'%(func.__name__,args))
        f.write('\n')
        f.close()
        return func(*args)
    return inner

@outer
def fun1(i):
    print(i+1)
    return i

@outer
def fun2(n,s):
    for i in range(n):
        print(s)

fun1(5)
fun2(3,'hello')
