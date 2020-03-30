#3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
import base64
f=open('student.txt','w')
for i in range(5):
    name=input('第'+str(i+1)+'个同学的姓名：')
    admin=input(name+'的账号是：')
    password=input(name+'的密码是：')
    a={'name':name,'admin':admin,'password':str(base64.b64encode(password.encode()))}
    f.write(str(a))
    f.write('\n')
f.close()

