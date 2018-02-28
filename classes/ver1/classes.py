class Thing():
    name = None #Name of Entity
    hp = None #Health
    dmg = None #Damage
    agi = None #Agility
    dfc = None #Defence
    mp = None #Magic Power(How much health you gain)
    mpu = None #Magic Power Usage(How many times you can heal

class Player(Thing):
    gold = 0 #Player has a gold stat because enemy does not need money

class Enemy(Thing):
    pass #Enemy is the exact same as it's parent(Thing) right now


