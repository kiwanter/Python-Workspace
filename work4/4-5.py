#5  通过Python来模拟实现一个txt文件的拷贝过程;
def mycopy(old,new):
    f=open(old,'r')
    f1=f.read()
    f.close()
    f=open(new,'w')
    f.write(f1)
    f.close()
mycopy('file.txt','copy.txt')