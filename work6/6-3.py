# 三、定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})
class dictclass():
    def __init__(self,data):
        self.__data=data
    def del_dict(self,key):
        print('delete',end=' ')
        print(key,end=':')
        print(self.__data.pop(key))
    def get_dict(self,key):
        if key in self.__data.keys():
            return self.__data[key]
        else:
            return 'not found'
    def get_key(self):
        return self.__data.keys()
    def get_data(self):
        return self.__data
    def update_dict(self):
        return self.__data.values()

test={'one':1,2:'two','three':'True'}
a=dictclass(test)
print(a.get_data())
print(a.get_dict('one'))
print(a.get_dict('three'))
print(a.get_key())
a.del_dict('three')
print(a.get_data())
print(a.update_dict())