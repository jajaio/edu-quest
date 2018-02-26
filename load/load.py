import json
import classes as cl
def loadGame():
    with open("player.json", "r") as pfile: #loads player.json file, and r reads it.
        j=json.load(pfile)
        cl.Player.hp = j["hp"]
        cl.Player.agi = j["agi"]
        cl.Player.dfc = j["dfc"]
        cl.Player.dmg = j["dmg"]
        cl.Player.mp = j["mp"]
        cl.Player.mpu=  j["mpu"]
        cl.Player.gold = j["gold"]
        cl.Player.name = j["name"]

if __name__ == "__main__":
    loadGame()
    print(cl.Player.name)
