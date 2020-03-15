a=int(input('输入年份：'))
if(a % 4 == 0 and a % 100 != 0):
    print("是闰年")
elif(a%400==0):
    print("世纪闰年")
else:
    print("普通年")