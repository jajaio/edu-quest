import classes as cl
import random

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
    enemy.hp += enemy.dfc

def playerHeal():
    if player.mpu < 1:
        print("You are out of Magic!")
        playerAttack()
    else:
        print("Player heals " + str(player.mp) + "HP!")
        player.hp += player.mp
        player.mpu -= 1

def enemyAttack():
    print("Enemy atttacks!")
    player.hp -= enemy.dmg
    player.hp += player.dfc

def enemyHeal():
    if enemy.mpu < 1: #Checks to see if Magic Power Usage is less than 1
        enemyAttack() #Attacks because Enemy can not heal
    else:
        print("Enemy heals " + str(enemy.hp) + " HP!")
        enemy.hp += enemy.mp 
        enemy.mpu -= 1

def playerMove():        
    print("Player HP: " + str(player.hp) + " Player MP: " + str(player.mpu))
    print("Enemy HP: " + str(enemy.hp) + " Enemy MP: " + str(enemy.mpu))
    prompt = input("Attack(1), Heal(2) >>>").strip()
    if prompt == "1":
        playerAttack()
    elif prompt == "2":
        playerHeal()
    else:
        print("You were confused!")

def enemyMove():
    move = random.randint(1, 2)
    if move == 1:
        enemyAttack()
    elif move == 2:
        enemyHeal()
                
def run():
    global player, monster
    while True:
        fight()

if __name__ == "__main__":
    cl.Player = cl.DefaultPlayer
    cl.Enemy = cl.Slime
    player = cl.Player()
    enemy = cl.Enemy()
    run()
