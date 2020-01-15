class hero:
    def __init__(self, name, health, attack, defense, speed, legs):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.legs = legs
       
class feline_hero(hero):
    def __init__(self, name):
        super().__init__(name, 150, 100, 70, 80, 4)

class reptile_hero(hero):
    def __init__(self, name):
        super(). __init__(name, 50, 200, 30, 50, 0)
class flying_hero(hero):
    def __init__(self, name):
        super(). __init__(name, 80, 150, 50, 200, 2)

doge = feline_hero('doge')
cate = feline_hero('cate')
snek = reptile_hero('snek')
owel = flying_hero('owel')

print(doge.__dict__)
print(cate.__dict__)
print(snek.__dict__)
print(owel.__dict__)