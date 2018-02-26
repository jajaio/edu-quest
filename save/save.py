import json #imports json file type
import classes as cl

def saveGame():
    with open('player.json', 'w') as pfile: #writes to player.json, w overwritesold save
        pfile.write(json.dumps({ #writes to json file
                "hp":cl.Player.hp, #json hp stat is equal to players hp
                "agi":cl.Player.agi,
                "dfc":cl.Player.dfc,
                "dmg":cl.Player.dmg,
                "mp":cl.Player.mp,
                "mpu":cl.Player.mpu,
                "gold":cl.Player.gold,
                "name":cl.Player.name
                }))

if __name__ == "__main__":
    saveGame()
