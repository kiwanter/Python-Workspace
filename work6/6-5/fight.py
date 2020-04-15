from dog import *
from human import *
import random
import time
humen=[human('m'),human('n')]
dogs=[dog('x'),dog('y'),dog('z')]
turn=random.randint(0,1)
while(True):
    if turn == 0:
        suffer=random.choice(humen)
        suffer.get_hurt(random.choice(dogs).get_ad())
        if suffer.get_hp()<=0:
            humen.remove(suffer)
        turn = 1
    elif turn == 1:
        suffer=random.choice(dogs)
        suffer.get_hurt(random.choice(humen).get_ad())
        if suffer.get_hp()<=0:
            dogs.remove(suffer)
        turn = 0
    time.sleep(0.05)
