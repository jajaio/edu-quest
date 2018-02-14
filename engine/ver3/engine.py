import classes as cl
from random import randint
import colors as c
from time import sleep as s

def hpScan():
    if player.hp < 1:
        print("You Died!")
        exit() #link to function later
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
    print(c.clear)
    print(c.blue + "Player attacks!")
    s(1)
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
    print(c.clear)
    print(c.red + "Enemy atttacks!")
    s(1)
    player.hp -= enemy.dmg
    player.hp += player.dfc

def enemyHeal():
    if enemy.mpu < 1:
        enemyAttack() 
    else:
        
        print("Enemy heals " + str(enemy.hp) + " HP!")
        enemy.hp += enemy.mp 
        enemy.mpu -= 1

def playerMove():        
    print(c.blue + "Player HP: " + str(player.hp) + " Player MP: " + str(player.mpu))
    print(c.red + "Enemy HP: " + str(enemy.hp) + " Enemy MP: " + str(enemy.mpu))
    prompt = input(c.yellow + "Attack(1), Heal(2) " + c.base2 + ">>>" + c.magenta).strip()
    if prompt == "1":
        playerAttack()
    elif prompt == "2":
        playerHeal()
    else:
        print("You were confused!")
        s(1)
        print(c.clear)

def enemyMove():
    move = randint(1, 2)
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
