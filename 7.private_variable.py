class Hero:
    # class variable
    jumlah = 0

    def __init__(self, name, health):
        self.name =name
        self.health = health

    # varibal private
    # self.__private = "private"
    
    # # varible instance protected
    # self._protected = "protected"
        
line = Hero("lina", 100)

print(line.__dict__)
# line._protected = 'testing'
# print(line.protected)
# print(line.__dict__)