import colors as c
from time import sleep as s
import save
#import town

def home():
    print(c.clear)
    print(c.yellow + "Welcome Home!")
    s(1)
    prompt = input("Would you like to save your game? Y/n" + c.magenta + " >>>").strip().lower()
    if prompt == "y":
        print(c.yellow + "Saving Game...")
        save.saveGame()
        print("Game saved!")
        continueGame()
    elif prompt == "n":
        print(c.yellow+"Returning to town.")
        s(1)
        #town.hub()
    else:
        print(c.yellow + "Invalid Input. Please respond with Y/n")
        s(2)
        home()

def continueGame():
    cont = input(c.yellow + "Would you like to exit the game? Y/n " + c.magenta + ">>>")
    if cont == "y":
        print(c.yellow + "Exiting Game")
        exit()
    elif cont == "n":
        print(c.yellow + "Returning to town.")
        s(1)
        #town.hub()
    else:
        print(c.yellow + "Invalid Input. Please respond with Y/n")
        s(2)
        continueGame()

if __name__ == "__main__":
    home()
