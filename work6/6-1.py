#一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
class dog():
    __data=[]
    def __init__(self,r:int,g:int,b:int):
        self.__data.append({'color':'red','number':r,'price':30})
        self.__data.append({'color':'green','number':g,'price':20})
        self.__data.append({'color':'blue','number':b,'price':40})
    def p(self):
        for t in self.__data:
            print('%s dog price %d now has %d' %(t['color'],t['price'],t['number']))
    def buy(self,c:str,n:int):
        for t in self.__data:
            if t['color']==c:
                t['number']+=n
                print('buy %s dog %d' %(c,n))
    def sell(self,c:str,n:int):
        for t in self.__data:
            if t['color']==c:
                t['number']-=n
                print('sell %s dog %d' %(c,n))    

a=dog(2,3,4)
a.p()
a.buy('red',3)
a.p()
a.sell('blue',2)
a.p()