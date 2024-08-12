class Mangga:
    # magic method 
    
    def __init__(self, name, jumlah):
        self.name = name
        self.jumlah = jumlah
        
    def __repr__(self):
        return "Debug : mangga: {},  dengan jumlah : {}".format(self.name, self.jumlah)
        

    def __str__(self):
        return "mangga: {},  dengan jumlah : {}".format(self.name, self.jumlah)
        
    def __add__(self, belanja):
        return self.jumlah + belanja.jumlah

    @property
    def __dict__(self):
        return "object ini mempunyai nama dan jumlah"
    
belanja1 = Mangga('arumanis',10)
belanja1 = Mangga('arumanis',10)
belanja2 = Mangga('mana lagi',5)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)