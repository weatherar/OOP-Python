class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def showInfo(self):
        print("{} dengan health : {}".format(self.name, self.health))
        
class Hero_inteligent(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)
        super().__init__(name, 100)
        super().showInfo()
        
class Hero_strenght(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 200)
        super().__init__(name, 200)
        super().showInfo()
        
Lina = Hero_inteligent('line')
axe = Hero_strenght('axe')

# print(Lina.name , "", Lina.health)
# print(axe.name , "", axe.health)
        
