class Thing():
    name = None #Name of Entity
    hp = None #Health
    dmg = None #Damage
    agi = None #Agility
    dfc = None #Defence
    mp = None #Magic Power(How much health you gain)
    mpu = None #Magic Power Usage(How many times you can heal

class Player(Thing):
    gold = 0 #Enemy does not need gold

class Enemy(Thing):
    reward = None #Player does not need to drop gold

class DefaultPlayer(Player): #Stats that the player is set to have at the start of the game
    #default player does not have a defined name stat because it is defined by the player at the beginning of the game
    hp = 10
    dmg = 5
    agi = 10
    dfc = 2
    mp = 1
    mpu = 1

class Rogue():
    hp = 15
    dmg = 8
    agi = 25
    dfc = 3
    mp = 3
    mpu = 2

class Warrior():
    hp = 25
    dmg = 10
    agi = 5
    dfc = 7
    mp = 3
    mpu = 1

class Mage():
    hp = 15
    dmg = 8
    agi = 15
    dfc = 2
    mp = 6
    mpu = 3

class Assassin():
    hp = 25
    dmg = 10
    agi = 100
    dfc = 5
    mp = 5
    mpu = 3

class Knight():
    pass

class Wizard():
    pass

class Slime(Enemy):
    name = "Slime"
    hp = 6
    dmg = 3
    agi = 5
    dfc = 1
    mp  = 2 
    mpu = 1
    reward = 10

def displayStats(input_character):
    stats = """
    Name: {p.name}
    Health Points: {p.hp}
    Damage: {p.dmg}
    Agility: {p.agi}
    Defense: {p.dfc}
    Magic Power: {p.mp}
    Magic Power Usage: {p.mpu}
    """
    print(stats.format(p = input_character))

if __name__ == "__main__":
    displayStats(Slime)
