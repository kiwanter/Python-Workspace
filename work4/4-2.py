# 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）
import datetime
def fun():
    datestr=input('日期（xxxx/xx/xx）')
    date=datetime.datetime.strptime(datestr,'%Y/%m/%d')
    a=date.isocalendar()
    print('是'+str(a[0])+'年的第'+str(a[1])+'周，星期'+str(a[2]))
    print('是校历的第'+str(a[1]-7)+'周，星期'+str(a[2]))
fun()