import classes as cl
import random

def hpScan():
    if player.hp < 1:
        print("You Died!")
        exit() #link to function later
    elif enemy.hp <1:
        print("You Win!")
        exit()

def fight():
    if player.agi >= enemy.agi: #check to see if player has more agility than the enemy
        playerMove() #if so, player moves first
        hpScan() #check to make sure the attack didn't kill the enemy
        enemyMove() #enemy moves
    else: #if the player has lower agility, then it is only possible for the enemy to attack first
        enemyMove()
        hpScan()
        playerMove()

def playerAttack():
    print("Player attacks!")
    enemy.hp -= player.dmg
    enemy.hp += enemy.dfc #enemy gains back the amount of health. total health lost = player's damage - enemy's defence

def playerHeal():
    if player.mpu < 1: #You can't attack if you are out of magicd 
        print("You are out of Magic!")
        playerAttack()
    else:
        print("Player heals " + str(player.mp) + "HP!")
        player.hp += player.mp #player gains the amount of health that it's  
        player.mpu -= 1 #magic power usage does down by one

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
    elif prompt == "2": #New option to heal
        playerHeal()
    else:
        print("You were confused!")

def enemyMove(): #Some AI has been added this time
    move = random.randint(1, 2) #randomly chooses 1 or 2
    if move == 1:
        enemyAttack()
    elif move == 2:
        enemyHeal()
                
def run():
    global player, monster
    while True:
        fight()

if __name__ == "__main__":
    cl.Player = cl.DefaultPlayer #player is set to be the default player class
    cl.Enemy = cl.Slime #enemy is set to be the slime class
    player = cl.Player()
    enemy = cl.Enemy()
    run()
