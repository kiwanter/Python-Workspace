'''list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
print(i for i in list1 if i in list2)

set1=set(list1)
set2=set(list2)
print(set1 & set2)'''

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
print([l for l in list1 if l in list2])