from concurrent.futures import ThreadPoolExecutor
import threading
import random
def fun():
    print('%s:%d' %(threading.current_thread().name, random.randint(0,100)))
    # print(random.randint(0,100))
    return 'finished'

# def test_result(future):
#     print(future.result())

def main():
    print('start')
    threadpool=ThreadPoolExecutor(max_workers=5,thread_name_prefix='fun_')
    for i in range(100):
        threadpool.submit(fun)
    threadpool.shutdown()

main()
    
