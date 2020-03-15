def dio(x):
    re={}
    for k,v in x.items():
        v=str(v)
        if len(v)>2:
            re[k]=v[0:2]
        else:
            re[k]=v
    return re

dict1={'a':1234,'b':1234,'c':1}
print(dio(dict1))