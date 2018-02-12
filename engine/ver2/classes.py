class Thing():
    hp = None
    dmg = None
    agi = None
    dfc = None
    mp = None
    name=None

class Player(Thing):
    gold = 0 

class Enemy(Thing):
    pass

class DefaultPlayer(Player):
    pass


