from Hero import HeroInteligent, HeroStrength
            
lina = HeroInteligent('lina')
slardar = HeroStrength('slardar')

lina.show_info()
slardar.show_info()

lina.gainExp = 200
slardar.gainExp = 250

lina.show_info()
slardar.show_info()