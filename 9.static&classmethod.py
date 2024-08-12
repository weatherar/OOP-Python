class Hero:

    # private class variables
    __jumlah = 0;
    
    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # methods ini tidak berlaku untuk object tapi berlaku untuk class
    def getJumlah(self):
        return Hero.__jumlah
    
    def getJumlah1():
        return Hero.__jumlah
    
     # static method decorator nempel ke object dan nempel ke kelasa nya
     
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
sniper = Hero('sniper')
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
drowranger = Hero('drowranger')
print(sniper.getJumlah2())
print(Hero.getJumlah3())