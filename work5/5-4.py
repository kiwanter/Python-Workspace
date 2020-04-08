def outera(func):
    def innera():
        print('无参数无返回值')
        func()
    return innera

def outerb(func):
    def innerb():
        print('无参数有返回值')
        a=func()
        return a
    return innerb

def outerc(func):
    def innerc(*args):
        print('有参数有返回值')
        a=func(*args)
        return a
    return innerc

def prime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True


@outera
def funa():
    print('20000内的素数')
    for i in range(20000):
        if prime(i):
            print(i,end=' ')
    print('\n')

@outerb
def funb():
    a=0
    for i in range(10000):
        if(prime(i)):
            a+=1
    return a

@outerc
def func(M):
    a=0
    for i in range(M):
        if(prime(i)):
            a+=1
    return a


funa()
print(funb())
print(func(15000))


