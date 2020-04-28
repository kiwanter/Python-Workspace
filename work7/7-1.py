import re
filea=open('webspiderUrl.txt',encoding='utf-8')
fileb=open('web.txt','w')
p=re.compile(r'(http.*(com|cn))')
for line in filea:
    data=p.findall(line)
    if len(data) > 0:
        fileb.write(data[0][0])
        fileb.write('\n')
filea.close()
fileb.close()