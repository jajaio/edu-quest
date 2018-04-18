import colors as c
from time import sleep as s
def hub():
    print(c.clear)
    print(c.yellow + "Welcome to the Town.")
    s(1)
    prompt = input("Would you like to go to the overworld(1), shop(2), or home?(3)").strip()
    if prompt == "1":
        pass
    elif prompt == "2":
        pass
    elif prompt == "3":
        pass
    else:
        print(c.yellow + "Invalid input. Please respond with a 1, 2, or 3.")
        s(2)
        hub()

def run():
    hub()

if __name__ == "__main__":
    run()
