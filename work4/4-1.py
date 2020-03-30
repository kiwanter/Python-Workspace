import time
from collections import deque
a=[1,2,3,4,5]
t1=time.time()
a.insert(0,0)
a.append(6)
print(a)
t2=time.time()
b=deque([1,2,3,4,5])
b.appendleft(0)
b.append(6)
print(b)
t3=time.time()
print('list时间：'+str(t2-t1))
print('deque时间：'+str(t3-t2))
print('相差时间：'+str(t3+t1-(t2*2)))