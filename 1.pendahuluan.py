class Hero : #
    # class varianles
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat hero dengan nama " + inputName)
        
hero1 = Hero("sniper",100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana" ,124,12 ,4)
print(Hero.jumlah)
hero3 = Hero("ucup" ,1000,100,0)
print(Hero.name)
