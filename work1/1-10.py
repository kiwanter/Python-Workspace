add=str(input('输入文件路径及名称：'))
filew=open(add)
file=filew.read()
filew.close()
file_list=file.split(' ')
print(file_list)
a={}
for i in file_list:
    if(i in a):
        a[i]=a[i]+1
    else:
        a[i]=1
print(a)