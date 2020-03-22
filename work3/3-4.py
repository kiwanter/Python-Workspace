import random
import string
import os
def raname():
    na=random.sample(string.ascii_letters+string.digits,5)
    return ''.join(na)
#print(os.getcwd())
os.mkdir('img')
for i in range(10):
    f=open('img/'+raname()+'.png','x')
    f.close()
basename=[os.path.splitext(filename)[0] for filename in os.listdir('img')]
#print(basename)
for filename in basename:
    old=os.path.join('img',str(filename)+'.png')
    new=os.path.join('img',str(filename)+'.jpg')
    os.rename(old,new)


