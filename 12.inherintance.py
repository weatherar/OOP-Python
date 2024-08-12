class Hero:
    def __init__(self, name, healt):
        self.name = name
        self.healt = healt

class Hero_inteligent(Hero):
    pass

class Hero_strenght(Hero):
    pass


lina = Hero('line',100)
techis = Hero_inteligent('techis',50)
axe = Hero_strenght('axe',100)
print(lina.name)
print(techis.name)
print(axe.name)
