# 六  用面向对象,实现一个学生Python成绩管理系统;
#       学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#       实现对学生信息及成绩的增,删,改,查方法;
import json
class student():
    __students=[]
    def __init__(self,data:list):
        self.__clbum=data[0]
        self.__num=data[1]
        self.__name=data[2]
        self.__score=data[3]
        self.__students.append(self)
    @classmethod
    def get_students(self):
        return self.__students
    def delete(self):
        student.__students.remove(self)
    def print_info(self):
        print('clbum:%s num:%s name:%s score:%s' %(self.__clbum,self.__num,self.__name,self.__score))

def read(url):
    f=open(url,'r')
    for x in f:
        student(json.load(x))
    f.close()

def write(url):
    f=open(url,'w')
    for x in student.get_students():
        json.dump(x,f)
    f.close()

# f=open('student.json','w')
# f.write(str(['A','01','a01','99']))
# print(list(str(['A','01','a01','99'])))
# f.write('\n')
# f.write(str(['A','03','a03','97']))
# f.write('\n')
# f.write(str(['B','01','b01','96']))
# f.write('\n')
# f.close()
# read('student.json')
# for x in student.get_students():
#     print(x)

