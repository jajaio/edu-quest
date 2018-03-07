class Thing():
    name = None #Name of Entity
    hp = None #Health
    dmg = None #Damage
    agi = None #Agility
    dfc = None #Defence
    mp = None #Magic Power(How much health you gain)
    mpu = None #Magic Power Usage(How many times you can heal

class Player(Thing):
    gold = 0 

class Enemy(Thing):
    pass

class DefaultPlayer(Player):
    hp = 10
    dmg = 5
    agi = 10
    dfc = 2
    mp = 1
    mpu = 1

class Slime(Enemy):
    name = "Slime"
    hp = 6
    dmg = 3
    agi = 5
    dfc = 1
    mp = 3
    mpu = 1
