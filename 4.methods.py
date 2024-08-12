class Hero :
    #class variabe
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, inputPower,inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
    # ?void function
    def siapa(self):
        print("namaku adalah" + self.name)
        

    # method dengan argument, tanpa return
    def healthUp(self,up):
        self.health += up
        
    # method dengan return
    def getHealth(self):
        return self.health
        
hero1 = Hero('sniper',100,10,5)
hero2 = Hero('mario',90,0,2) 

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
hero1.healthUp(100)

print(hero1.getHealth())