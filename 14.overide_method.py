class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def showInfo(self):
        print('shoe info di class Hero')
        print("{} ,\n\t health : {}".format(self.name, self.health))
        
class Hero_inteligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
        
# override inheritance
    def showInfo(self):
        print('shoew info di  subclass Hero')
        print("{}\n\t Tipe : intelegent,\n\thealth: {}".format(self.name,self.health))
        
class Hero_strenght(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        
lina = Hero_inteligent('lina')
axe = Hero_strenght('axe')

lina.showInfo()
axe.showInfo()