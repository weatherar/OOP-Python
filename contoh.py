# 16. multiple inherintance

class Team:
    def setTeam(self, team):
        self.team = team
        
    def showTeam(self):
        print(self.team)

class Tipe_Hero:
    def setTipeHero(self, tipeHero):
        self.tipeHero = tipeHero

    def showTipeHero(self):
        print(self.tipeHero)


class Hero(Team, Tipe_Hero):
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
ucup = Hero('ucup',100)
ucup.setTeam('merah')
ucup.setTipeHero('cundang')

ucup.showTeam()
ucup.showTipeHero()