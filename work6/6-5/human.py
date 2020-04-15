from sys import exit
class human():
    __alive=0
    def __init__(self,name:str):
        self.__name=name
        self.__hp=100
        self.__ad=10
        human.__alive+=1
    def get_alive(self):
        return human.__alive
    def get_hp(self):
        return self.__hp
    def get_ad(self):
        return self.__ad
    def get_hurt(self,damage:int):
        self.__hp-=damage
        self.__ad-=2
        if self.__ad < 1:
            self.__ad = 1
        print('%s(human) get %d hurt' %(self.__name,damage))
        print('%s(human) now has %d hp %d ad' %(self.__name,self.__hp,self.__ad))
        if self.__hp <= 0:
            print('%s(human) is dead' %(self.__name))
            human.__alive-=1
            if human.__alive <= 0:
                print('dog win')
                exit(0)