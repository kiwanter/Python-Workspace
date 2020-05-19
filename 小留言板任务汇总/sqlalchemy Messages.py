# 3  对2中的表结构，用SQLAchemy模块来实现同样的操作；
#encoding: utf-8
import sqlalchemy
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DIALCT = "mysql"
DRIVER = "mysqlconnector"
HOSTNAME='127.0.0.1'
PORT='3306'
DATABASE='test'
USERNAME='root'
PASSWORD='123456'

Base=declarative_base()
class messages(Base):
    # 表的名字:
    __tablename__ = 'messages'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    message = Column(String(255))
    user = Column(String(20))
    time = Column(String(30))
    is_deleted = Column(Integer)
# class SQLAMessages(Base):
#     # 表的名字:
#     __tablename__ = 'SQLAMessage'
#
#     # 表的结构:
#     id = Column(Integer, primary_key=True)
#     message = Column(String(255))
#     name = Column(String(20))
#     is_deleted = Column(Integer)
#dialect+driver://username:password@host:port/database
DB_URI="{dialct}+{driver}://{username}:{password}@{hostname}:{port}/{database}".format(dialct=DIALCT,driver=DRIVER,username=USERNAME,password=PASSWORD,hostname=HOSTNAME,port=PORT,database=DATABASE)
print(DB_URI)
try:
    engine=create_engine(DB_URI)
    DBSession=sessionmaker(bind=engine)
except Exception as e:
    exit('数据库链接错误')

def query():
    id=input('输入要查询的ID：')
    try:
        session=DBSession()
        x=session.query(messages).filter(messages.id==id).one()
    except:
        exit("数据库操作异常")
    #print('type:'+type(x))
    print('message:'+x.message)
    print('user:'+x.user)

def add():
    USER=input('输入用户名：')
    MESSAGE=input('输入留言：')
    try:
        session=DBSession()
        new_message=messages(message=MESSAGE,user=USER,is_deleted=0)
        session.add(new_message)
        session.commit()
        session.close()
    except:
        exit("数据库操作异常")
    print('操作成功')

def delete():
    ID=input('请输入要删除的ID：')
    try:
        session=DBSession()
        session.query(messages).filter(messages.id==ID).update({"is_deleted":1})
        session.commit()
        session.close()
    except:
        exit("数据库操作异常")
    print('操作成功')

def update():
    ID = input('请输入要修改的ID：')
    new_message=input('输入新留言：')
    try:
        session = DBSession()
        session.query(messages).filter(messages.id == ID).update({"message": new_message})
        session.commit()
        session.close()
    except:
        exit("数据库操作异常")
    print('操作成功')

if __name__ == '__main__':
    #query()
    #add()
    #delete()
    update()

