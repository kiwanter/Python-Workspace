#coding=utf-8
from  flask import Flask,request,render_template
import pymysql
import datetime
from configparser import ConfigParser

#读取配置文件
try:
    config = ConfigParser()
    config.read('config.ini')
    host=config.get('mysql','host')
    port=config.get('mysql','port')
    user=config.get('mysql','user')
    password=config.get('mysql','password')
    database=config.get('mysql','database')
except:
    print('配置文件加载失败')

#flask实例
app=Flask(__name__)

#连接数据库
try:
    # conn=pymysql.connect(host=host,
    #                      port=port,
    #                      user=user,
    #                      password=password,
    #                      database=database,
    #                      charset='utf8')
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='123456',
                           database='web messages',
                           charset='utf8')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
except:
    print('数据库连接失败')



@app.route('/')
def index():
    return render_template('index.html',info='请输入用户名和密码')

@app.route('/login',methods=['POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    sql="select * from userdata where username = %s and password = %s"
    try:
        rows=cursor.execute(sql,(username,password))
        if rows == 0:
            return render_template('index.html',info='登陆失败，请重新登录')
        else:
            return render_template('login.html',user=username,indo='请输入留言',lst=query())
    except:
        return render_template('index.html', info='数据库异常，无法登陆')

@app.route('/register')
def register():
    return render_template('register.html',info='输入信息注册新的账号')

@app.route('/registersf',methods=['POST'])
def registersf():
    username=request.form.get('username')
    password=request.form.get('password')
    sql="select * from userdata where username = %s"
    try:
        rows=cursor.execute(sql,(username))
        if rows > 0:
            return render_template('register.html',info='该用户名已存在')
        else:
            sql='Insert into userdata (username,password) values (%s,%s)'
            cursor.execute(sql,(username,password))
            conn.commit()
            return render_template('index.html',info='注册成功,请登陆')
    except:
        return render_template('index.html',info='数据库异常，无法注册')

@app.route('/message',methods=['POST','GET'])
def message():
    message=request.form.get('message')
    username=request.form.get('username')
    if message and username:
        try:
            time=datetime.datetime.now()
            sql="Insert into messagesdata (username,messages,datetime) values (%s,%s,%s)"
            rows=cursor.execute(sql,(username,message,time))
            if rows == 1:
                conn.commit()
                return render_template('login.html',user=username,info='留言成功',lst=query())
            else:
                return render_template('login.html', user=username, info='数据库异常无法留言',lst=query())
        except:
            return render_template('login.html',user=username,info='数据库异常无法留言',lst=query())
    else:
        return render_template('login.html', user=username, info='请输入留言',lst=query())

#将数据库的数据转化为列表格式
def query():
    sql = "select * from messagesdata"
    cursor.execute(sql)
    data = cursor.fetchall()
    lst = []
    for x in data:
        t = [x['username'], x['messages'], x['datetime']]
        lst.append(t)
    return lst

if __name__ == '__main__':
    app.run()