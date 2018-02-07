import classes as cl

def hpScan():
    if player.hp < 1:
        print("You Died!")
        exit()
    elif enemy.hp <1:
        print("You Win!")
        exit()

def fight():
    if player.agi >= enemy.agi:
        playerMove()
        hpScan()
        enemyMove()
    else:
        enemyMove()
        hpScan()
        playerMove()

def playerAttack():
    print("Player attacks!")
    enemy.hp -= player.dmg

def enemyAttack():
    print("Enemy atttacks!")
    player.hp -= enemy.dmg
    
def playerMove():        
    print("Player HP: " + str(player.hp))
    print("Enemy HP: " + str(enemy.hp))
    prompt = input("Attack(1) >>>").strip()
    if prompt == "1":
        playerAttack()
    else:
        print("You were confused!")


def enemyMove():
    enemyAttack()
    #add more later
                
def run():
    global player, monster
    while True:
        fight()

if __name__ == "__main__":
    player = cl.Player()
    enemy = cl.Enemy()
    run()
