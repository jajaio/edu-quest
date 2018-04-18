import colors as c
from time import sleep as s
import save

def home():
    print(c.clear)
    print("Welcome Home!")
    s(1)
    prompt = input("Would you like to save your game? Y/n" + c.magenta +" >>>").strip().lower()
    if prompt == "y":
        print(c.yellow + "Saving Game...")
        save.saveGame()
        print("Game saved!")
        cont = input("Would you like to exit the game?")
        if cont == "y":
            print("Exiting Game")
            exit()
        if cont == 
    elif prompt == "n":
        pass
    else:
        print(c.yellow + "Invalid Input. Please respond with Y/n")
        s(2)
        home()


if __name__ == "__main__":
    pass
