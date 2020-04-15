# 二 定义一个学生Student类。有下面的类属性：
# 1 姓名 name
# 2 年龄 age
# 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:
class student():
    __regmen=0
    def __init__(self,name:str,age:int,score:list):
        self.__regmen+=1
        self.__name=name
        self.__age=age
        self.__score=score
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_course(self):
        return max(self.__score)

a=student('Tom',19,[75,80,90])
print(a.get_name())
print(a.get_age())
print(a.get_course())