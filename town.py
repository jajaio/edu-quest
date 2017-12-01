import classes as cl
import save
import time as t
import colors as c
import field as f
import load
import tower

author='jajaio'

def saveArea():
    print(c.clear)
    innq=input(c.yellow+"Welcome to the Save Area. Would you like to rest here? Or leave? (1), (2)"+c.reset+">>>"+c.violet).strip()
    if innq=="1":
        print(c.yellow+"You save your game.")
        t.sleep(.5)
        cl.show_player()
        print("[Game saved!]")
        save.save_game()
        qu=input('[Would you like to keep playing?] (Y/N)'+c.reset+' >>>'+c.violet).strip().lower()
        if qu=='y':
            print(c.yellow+'[Resuming game]')
        elif qu=='n':
            print(c.yellow+'[Exiting game...]')
            exit()
        else:
            print(c.yellow+'[Resuming game]')
        print(c.yellow+"You are back in the game.")
        t.sleep(1.5)
        hub()
    elif innq=="2":
        print(c.yellow+"You return to the Hub Area.")
        t.sleep(1)
        hub()
    else:
        print(c.yellow+"I don't understand...")
        t.sleep(1)
        inn()

def hub():
    save.save_game()
    print(c.clear)
    print(c.yellow+"Welcome to the Hub Area!")
    hubQuestion=input("Would you like to go to the field, shop, save area, or the boss arena? (1), (2), (3), (4)"+c.reset+" >>>"+c.violet)
    if hubQuestion=="1":
        print(c.yellow+"You decide to go to the field.")
        t.sleep(1.3)
        f.field()
    elif hubQuestion=="2":
        print(c.yellow+"You decide to go to the shop.")
        t.sleep(1.3)
        shop()
    elif hubQuestion=="3":
        print(c.yellow+"You decide to go to the save area.")
        t.sleep(1.3)
        inn()
    elif hubQuestion=="4":
        print(c.yellow+"You decide to go to the boss arena.")
        t.sleep(1.25)
        tower.tower()
    else:
        print("I don't understand...")
        t.sleep(1)
        hub()

def shop():
    print(c.clear)
    while True:
        shopQuestion=input(c.yellow+"Welcome to the shop! Would you like to see low tier classes, high tier classes, or would you like to leave? (1), (2), (3)"+c.reset+" >>>"+c.violet).strip()
        if shopQuestion=="1":
            lowTierPrompt=input(c.yellow+"Okay, would you like to see the the Rouge, Cleric, or Tank? (1),(2),(3)"+c.reset+" >>>"+c.violet).strip()
            if lowTierPrompt=="1":
                cl.show_rogue()
                buyRouge=input(c.yellow+"You currently have "+str(cl.Player.gold)+" gold. Would you like to purchase the Rogue class for 100 gold? (Y/N)"+c.reset+" >>>"+c.violet).strip().lower()
                if buyRouge=="y":
                    if int(cl.Player.gold) >= 100:
                        cl.Player.hp=cl.Rogue.hp
                        cl.Player.att=cl.Rogue.att
                        cl.Player.agi=cl.Rogue.agi
                        cl.Player.deff=cl.Rogue.deff
                        cl.Player.mp=cl.Rogue.mp
                        cl.Player.gold-=100
                        print(c.yellow+"You are now a Rogue!")
                        t.sleep(1)
                        cl.show_player()
                        print()
                        save.save_game()
                        input("[Game saved! Press enter to continue.]")
                        hub()
                    if int(cl.Player.gold) < 100:
                        print(c.yellow+"You need more money! You currently have "+str(cl.Player.gold)+" and you need 100!")
                        input("[Press enter to continue.]")
                        hub()
                elif buyr=="n":
                    print(c.yellow+"Oh, okay.")
                    t.sleep(1)
                    shop()
            elif lowTierPrompt=="2":
                cl.show_cleric()
                buyCleric=input(c.yellow+"You currently have "+str(cl.Player.gold)+" gold. Would you like to purchase the Cleric class for 100 gold? (Y/N)"+c.reset+" >>>"+c.violet).strip().lower()
                if buyCleric=="y":
                    if int(cl.Player.gold) >= 100:
                        cl.Player.hp=cl.Cleric.hp
                        cl.Player.att=cl.Cleric.att
                        cl.Player.agi=cl.Cleric.agi
                        cl.Player.deff=cl.Cleric.deff
                        cl.Player.mp=cl.Cleric.mp
                        cl.Player.gold-=100
                        print(c.yellow+"You are now a Cleric!")
                        t.sleep(1)
                        cl.show_player()
                        print()
                        save.save_game()
                        input("[Press enter to continue.]")
                        hub()
                    elif int(cl.Player.gold) <= 100:
                        print(c.yellow+"You need more money! You currently have "+str(cl.Player.gold)+" and you need 100!")
                        hub()
                elif buyCleric=="n":
                    print(c.yellow+"Oh, okay.")
                    t.sleep(1)
                    shop()
            elif lowTierClass=="3":
                cl.show_sellsword()
                buyTank=input(c.yellow+"You currently have "+str(cl.Player.gold)+" gold. Would you like to purchase the Sellsword class for 100 gold? (Y/N)"+c.reset+" >>>"+c.violet).strip().lower()
                if buyTank=="y":
                    if int(cl.Player.gold) >= 100:
                        cl.Player.hp=cl.Tank.hp
                        cl.Player.att=cl.Tank.att
                        cl.Player.agi=cl.Tank.agi
                        cl.Player.deff=cl.Tank.deff
                        cl.Player.mp=cl.Tank.mp
                        cl.Player.gold-=100
                        print(c.yellow+"You are now a Tank!")
                        t.sleep(1)
                        cl.show_player()
                        print()
                        save.save_game()
                        input("[Game saved! Press enter to continue.]")
                        hub()
                    elif int(cl.Player.gold) <= 100:
                        print(c.yellow+"You need more money! You currently have "+str(cl.Player.gold)+" and you need 100!")
                        input("[Press enter to continue]")
                        hub()
                elif buyTank=="n":
                    print(c.yellow+"Oh, okay.")
                    t.sleep(1)
                    shop()
                else:
                    print(c.yellow+"I'm not sure if I understand...")
                    t.sleep(1.25)
                    shop()
        elif question=="2":
            question_q=input(c.yellow+"Our masteries are the Assassin, Wizard, Paladin. What would you like to see? (1), (2), (3)"+c.reset+" >>>"+c.violet).strip()
            if question_q=="1":
                cl.show_assassin()
                buyg=input(c.yellow+"You currently have "+str(cl.Player.gold)+" gold. Would you like to purchase the Assassin class for 200 gold? (Y/N)"+c.reset+" >>>"+c.violet).strip().lower()
                if buyg=='y':
                    if int(cl.Player.gold) >= 200:
                        cl.Player.hp=cl.Assassin.hp
                        cl.Player.att=cl.Assassin.att
                        cl.Player.agi=cl.Assassin.agi
                        cl.Player.deff=cl.Assassin.deff
                        cl.Player.mp=cl.Assassin.mp
                        cl.Player.gold-=200
                        print(c.yellow+"You are now an Assassin!")
                        t.sleep(1)
                        cl.show_player()
                        print()
                        save.save_game()
                        input("[Game saved! Press enter to continue.]")
                        hub()
                    elif int(cl.Player.gold) <= 200:
                        print(c.yellow+"You need more money! You currently have "+str(cl.Player.gold)+" and you need 200!")
                        input("[Press enter to continue.]")
                        hub()
                elif buyg=='n':
                    print(c.yellow+"Oh, okay.")
                    t.sleep(1)
                    shop()
                else:
                    print("I'm not sure if I understand...")
                    t.sleep(1.25)
                    shop()
            elif question_q=="2":
                cl.show_wizard()
                buyh=input(c.yellow+"You currently have "+str(cl.Player.gold)+" gold. Would you like to purchase the Wizard class for 200 gold? (Y/N)"+c.reset+" >>>"+c.violet).strip().lower()
                if buyh=="y":
                    if int(cl.Player.gold) >= 200:
                        cl.Player.hp=cl.Wizard.hp
                        cl.Player.att=cl.Wizard.att
                        cl.Player.agi=cl.Wizard.agi
                        cl.Player.deff=cl.Wizard.deff
                        cl.Player.mp=cl.Wizard.mp
                        cl.Player.gold-=200
                        print(c.yellow+"You are now a Wizard!")
                        t.sleep(1)
                        cl.show_player()
                        print()
                        save.save_game()
                        input("[Game saved! Press enter to continue.]")
                        hub()
                    elif int(cl.Player.gold) <= 200:
                        print(c.yellow+"You need more money! You currently have "+str(cl.Player.gold)+" and you need 200!")
                        input("[Press enter to continue.]")
                        hub()
                elif buyh=="n":
                    print("Oh, Okay.")
                    t.sleep(1)
                    shop()
                else:
                    print("I'm not sure if I understand...")
                    t.sleep(1.25)
            elif question_q=="3":
                cl.show_paladin()
                buyj=input(c.yellow+"You currently have "+str(cl.Player.gold)+" gold. Would you like to purchase the Paladin class for 200 gold? (Y/N)"+c.reset+" >>>"+c.violet).strip().lower()
                if buyj=="y":
                    if int(cl.Player.gold) >= 200:
                        cl.Player.hphp=cl.Paladin.hp
                        cl.Player.att=cl.Paladin.att
                        cl.Player.agi=cl.Paladin.agi
                        cl.Player.deff=cl.Paladin.deff
                        cl.Player.mp=cl.Paladin.mp
                        cl.Player.gold -= 200
                        print("You are now a Paladin!")
                        t.sleep(1)
                        cl.show_player()
                        print()
                        save.save_game()
                        input('[Game saved! Press enter to continue.]')
                        hub()
                    elif int(cl.Player.gold) <= 200:
                        print(c.yellow+"You need more money! You currently have "+str(cl.Player.gold)+" and you need 200!")
                        input('[Press enter to continue.]')
                        hub()
                elif buyj=="n":
                    print("Oh, Okay.")
                    t.sleep(1)
                    shop()
            else:
                print(c.yellow+"I'm not sure if I understand...")
                t.sleep(1.25)
                shop()
        elif question=="3":
            print(c.yellow+"You decide to go back to the town.")
            t.sleep(1.25)
            hub()
        else:
            print(c.yellow+"I'm not sure if I understand...")
            t.sleep(1.25)
            shop()
if __name__=='__main__':
    hub()
