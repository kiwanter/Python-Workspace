print('认证码:aaaaa')

def outer(func):
    def inner(*args):
        a=input('输入认证码：')
        if a == 'aaaaa':
            return func(*args)
        else:
            print('错误')
    return inner

@outer
def func(i):
    print(i*2)

func(6)