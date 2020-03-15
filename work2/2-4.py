def countstr(string):
    char,digit,space,other=0,0,0,0
    for i in string:
        if i.isalpha():char+=1
        elif i.isdigit():digit+=1
        elif i.isspace():space+=1
        else:other+=1
    return char,digit,space,other

print(countstr("1122 acwd 32 ().,"))