from sys import exit
class dog():
    __alive=0
    def __init__(self,name:str):
        self.__name=name
        self.__hp=80
        self.__ad=15
        dog.__alive+=1
    def get_alive(self):
        return dog.__alive
    def get_hp(self):
        return self.__hp
    def get_ad(self):
        return self.__ad
    def get_hurt(self,damage:int):
        self.__hp-=damage
        self.__ad-=3
        if self.__ad < 1:
            self.__ad = 1
        print('%s(dog) get %d hurt' %(self.__name,damage))
        print('%s(dog) now has %d hp %d ad' %(self.__name,self.__hp,self.__ad))
        if self.__hp <= 0:
            print('%s(dog) is dead' %(self.__name))
            dog.__alive-=1
            if dog.__alive <= 0:
                print('human win')
                exit(0)