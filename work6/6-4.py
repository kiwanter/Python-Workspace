# 四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#       封装方法，求单个学生的总分，平均分，以及打印学生的信息
class student():
    __count=0
    def __init__(self,name:str,age:int,sex:str,score:list):
        self.__count+=1
        self.__name=name
        self.__age=age
        self.__sex=sex
        self.__score=score
    def get_sum(self):
        return sum(self.__score)
    def get_avg(self):
        return sum(self.__score)/len(self.__score)
    def print_info(self):
        print('name:%s age:%d sex:%s score:%s' %(self.__name,self.__age,self.__sex,str(self.__score)))

a=student('aaa',19,'male',[80,85,87])
print(a.get_sum())
print(a.get_avg())
a.print_info()