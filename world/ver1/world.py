import classes as cl
from random import choice
from time import sleep as s
import colors as c


def randomMonster():
    enemies = [cl.Slime, cl.Skeleton]
    enemy = choice(enemies)
    cl.Enemy = enemy

def world():
    print(c.clear)
    print(c.yellow + "You enter the open world.")
    s(1)
    while True:
        prompt = input("Do you want to fight monsters?(1) Or head back to town?(2)" + c.base2 + " >>>" + c.magenta).strip()
        if prompt == "1":
            print("You decide to fight monsters.")
            print("You found a...")
            randomMonster()
            print(enemy.name + "!")
        elif prompt == "2":
            pass
        else:
            print(c.yellow)
            print("I don't understand... please answer with a 1 or a 2.")
            input("[Press enter to continue]")

if __name__ == "__main__":
    world()
