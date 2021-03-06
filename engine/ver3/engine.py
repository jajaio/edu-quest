import classes as cl
from random import randint
import colors as c #imports colors mod as var c
from time import sleep as s #imports sleep function from time as var s

def hpScan():
    if player.hp < 1:
        print(c.yellow + "You Died!")
        print(c.reset) #resets color so it doesn't bleed
        s(1) #sleeps for one second
        exit() #link to function later
    elif enemy.hp <1:
        print(c.yellow + "You Win!")  #prints in yellow
        s(1)
        goldAdd = randint(1, 20) #random int between 1 and 20
        player.gold += goldAdd #adds the earned gold to the player's gold stat
        print("You got " + str(goldAdd) + " gold!")
        print(c.reset)
        s(1)
        exit()

def agiScan():
    if player.agi >= enemy.agi:
        playerMove()
        hpScan()
        enemyMove()
        hpScan()
    elif player.agi < enemy.agi:
        enemyMove()
        hpScan()
        playerMove()
        hpScan()

def playerMove():
    if prompt == "1":
        playerAttack()
    elif prompt == "2":
        playerHeal()
    else:
        print(c.yellow + "You were confused!")
        s(1)

def playerAttack():
    print(c.blue + "Player attacks!")
    s(1)
    enemy.hp -= player.dmg
    enemy.hp += enemy.dfc
    
def playerHeal():
    if player.mpu < 1:
        print(c.yellow + "You are out of Magic!")
        s(1)
        playerAttack()
    else:
        print(c.blue + "Player heals " + str(player.mp) + "HP!")
        s(1)
        player.hp += player.mp
        player.mpu -= 1

def enemyAttack():
    print(c.red + "Enemy atttacks!")
    s(1)
    player.hp -= enemy.dmg
    player.hp += player.dfc

def enemyHeal():
    if enemy.mpu < 1:
        enemyAttack() 
    else: 
        print(c.red + "Enemy heals " + str(enemy.hp) + " HP!")
        s(1)
        enemy.hp += enemy.mp 
        enemy.mpu -= 1

def fight():        
    print(c.clear)
    print(c.blue + player.name + " HP: " + str(player.hp) + " " + player.name + " MP: " + str(player.mpu)) #player's color theme is blue
    print(c.red + enemy.name + " HP: " + str(enemy.hp) + " " + enemy.name + " MP: " + str(enemy.mpu)) #enemy's is red
    global prompt 
    prompt = input(c.yellow + "Attack(1), Heal(2) " + c.base2 + ">>>" + c.magenta).strip()
    agiScan()

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
    player.name = "Jon Appleseed" #if player doesn't have a name, make it Jon Appleseed.
    run()
