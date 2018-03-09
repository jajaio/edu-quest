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
    reward = None

class DefaultPlayer(Player): #Stats that the player is set to have at the start of the game
    #default player does not have a defined name stat because it is defined by the player at the beginning of the game
    hp = 10
    dmg = 5
    agi = 10
    dfc = 2
    mp = 1
    mpu = 1

class Rouge():
    hp = 15
    dmg = 8
    agi = 30
    dfc = 3
    mp = 3

class Warrior():
    pass

class Mage():
    pass

class Slime(Enemy):
    name = "Slime"
    hp = 6
    dmg = 3
    agi = 5
    dfc = 1
    mp 
    mpu = 1
    reward = 10

