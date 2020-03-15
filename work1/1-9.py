import random
import sys
answer=random.randint(1,10)
for i in range(5):
    a=int(input("猜测一个1-10之间的数，还有%d次机会"%(5-i)))
    if(a==answer):
        print('猜对了，游戏胜利')
        sys.exit(0)
print('游戏失败，答案是%d'%(answer))