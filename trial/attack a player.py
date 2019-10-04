import random

class Enemy:
    hp = 200
    def __init__(self, atkl, atkh):
    
        self.atkl = atkl
        self.atkh = atkh
    def getatk(self):
        print(self.atkl)
    def gethp(self):
        print(self.hp)


Enemy1 = Enemy(10,30)
print(Enemy1.atkh)
Enemy1.getatk()

enemy2 = Enemy(90,300)
enemy2.gethp()
print(enemy2.atkh)
















'''
playerhp = 300
enemyatklow = 20
enemyatkhigh = 60

while playerhp > 0:
    dmg = random.randrange(enemyatklow,enemyatkhigh)
    playerhp= playerhp - dmg

    if playerhp<=30:
        playerhp=30

    print("Enemy deals attack for", dmg, "points of damage. Current HP is", playerhp) 
       
        
    if playerhp > 30:
        continue

    print("HP dangerously low. Getting you out")
    break

'''