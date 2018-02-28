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
    prompt = input("Do you want to fight monsters? Or head back to town?" + c.white + " >>>" + c.magenta)
    

if __name__ == "__main__":
    print(c.yellow + "yuh")
