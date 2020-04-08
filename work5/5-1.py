import time
def outer(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print(end-start)
    return inner()

@outer
def fun():
    time.sleep(2)

fun