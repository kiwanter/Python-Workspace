#4  (继续上面的练习) 模拟用户登录:
#    5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);
import sys
import base64
name=[]
admin=[]
password=[]
f=open('student.txt','r')
for i in range(5):
    d=eval(f.readline())
    name.append(d['name'])
    admin.append(d['admin'])
    password.append(d['password'])
f.close()
#print(name)
#print(admin)
#print(password)
name_input=input('姓名：')
if name_input in name:
    for i in range(5):
        if name[i] == name_input:
            n=i
    admin_input=input('用户名：')
    if admin_input == admin[n]:
        password_input=input('密码：')
        if  password[n] == str(base64.b64encode(password_input.encode())):
            print('登陆成功')
            sys.exit(0)
        #else:
            #print(str(base64.b64encode(password[n].encode()))) 
print('登陆失败')