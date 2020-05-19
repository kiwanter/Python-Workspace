# 2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#    使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；


import  pymysql
import  datetime

try:
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='test',charset='utf8')#没有‘-’
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
except:
    exit('数据库连接失败')

#添加数据
def add():
    sql="INSERT INTO Messages (message,user,time,is_deleted) VALUES (%s,%s,%s,0)"
    user=input('用户名：')
    message=input('留言内容：')
    now_time = str(datetime.datetime.now())
    try:
        rows=cursor.execute(sql,(message,user,now_time))
        conn.commit()
    except:
        exit('数据库处理错误')
    print('操作成功')

#查询数据
def query():
    sql='SELECT * FROM Messages Where user = %s and is_deleted = 0'
    name=input('输入要查询的用户名：')
    try:
        rows=cursor.execute(sql,name)
    except:
        exit('数据库处理错误')
    for x in cursor.fetchall():
        print('id:'+str(x['id'])+',message:'+str(x['message']))

#删除数据(设置is_deleted为1)
def delete():
    sql='UPDATE Messages SET is_deleted = 1 Where id = %s'
    id=int(input('输入要删除的留言ID：'))
    try:
        rows=cursor.execute(sql,id)
        conn.commit()
    except:
        exit('数据库处理错误')
    print('操作成功')

#修改数据
def update():
    sql="UPDATE Messages SET message = %s Where id = %s"
    id=int(input('输入要修改的留言ID:'))
    message=input('输入新的留言：')
    try:
        rows=cursor.execute(sql,(message,id))
        conn.commit()
    except:
        exit('数据库处理错误')
    print('操作成功')

if __name__ == '__main__':
    # add()
    # query()
    # delete()
    update()
    conn.close()

