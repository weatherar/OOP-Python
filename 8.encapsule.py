# encapsulasi
# buat semua variable private
# memakai getter(mengambil varible) dan setter
class Hero:
    def __init__(self, name, health,attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower
        
    # getter
    def getName(self):
        return self.__name
    def getHealth(self):
        return self.__health
    # seeter
    def diserang(self, serangPower):
        self.__health -= serangPower
        
    def setAttackPower(self, nilaibaru):
        self.__attackPower = nilaibaru
        
    
# awal dari game
artchecker = Hero("archeker",50,5)
print(artchecker.__dict__)

# game berjalan
print(artchecker.getName())
artchecker.diserang(5)
print(artchecker.getHealth())