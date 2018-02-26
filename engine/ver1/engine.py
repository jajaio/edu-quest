import classes as cl #imports our character stats from the classes file

def hpScan(): #func for checking if the player/enemy is dead
    if player.hp < 1:
        print("You Died!")
        exit() #exit program
    elif enemy.hp < 1:
        print("You Win!")
        exit()

def fight(): #func for organizing the fight
        playerMove()
        hpScan()
        enemyMove()
        hpScan()

def playerAttack(): #player's attack move
    print("Player attacks!")
    enemy.hp -= player.dmg #enemy loses health based off of how much damage the player does

def enemyAttack(): #enemy's attack move
    print("Enemy atttacks!")
    player.hp -= enemy.dmg
    
def playerMove():        
    print("Player HP: " + str(player.hp)) #presenting the statistics, printing a string because hp is an int
    print("Enemy HP: " + str(enemy.hp))
    prompt = input("Attack(1) >>>").strip() #selecting move, .strip() removes un needed spaces
    if prompt == "1": 
        playerAttack()
    else:
        print("You were confused!") #if you don't select a move


def enemyMove(): #a bit redundant now, but func is made for organizing later
    enemyAttack()
                
def run():#running the fight
    global player, monster #sets vars global for the whole program
    while True:
        fight()

if __name__ == "__main__":
    player = cl.Player() #sets vars equal to the class
    enemy = cl.Enemy()
    run()
