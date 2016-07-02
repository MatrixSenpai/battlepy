import pickle
import os
from subprocess import call
from GameManager import GameManager
from Player import Player

player = ""

battleFileExt = ".bpydata"
playerDataFile = "./.playerdata%s" % battleFileExt
gameDataFile = "./.gameDataFile%s" % battleFileExt

def mainMenu():
    global player
    print "-" * 80
    print "Welcome back, %s" % player.name
    print "\n\n Main Menu"
    print "1) New Game"
    print "2) My Statistics"
    print "3) Change Name"
    print "4) Quit"
    choice = raw_input("> ")
    return int(choice)

def main():
    global player

    print "Loading..."

    pname = ""

    # Load player data if exists
    if os.path.isfile(playerDataFile):
        with open(playerDataFile, 'rb') as d:
            player = pickle.load(d)

    if os.path.isfile(gameDataFile):
        with open(gameDataFile, 'rb') as d:
            board = pickle.load(d)

    call(["clear"])

    print  "+" + "-" * 86 + "+"

    print  "|  BBBB      A     TTTTTT  TTTTTT  LL      EEEEE    SSSSS    HH  HH   IIIIII   PPPPPP  |"
    print  "|  B  B     A A      TT      TT    LL      EE       SSS      HH  HH     II     PP   P  |"
    print  "|  B B     AAAAA     TT      TT    LL      EEE        SSS    HHHHHH     II     PPPPPP  |"
    print  "|  B  B   AA   AA    TT      TT    LL      EE          SS    HH  HH     II     PP      |"
    print  "|  BBBB  AA     AA   TT      TT    LLLLLL  EEEEE    SSSSS    HH  HH   IIIIII   PP      |"

    print  "+" + "-" * 86 + "+\n"

    if player == "":
        print "Please create a player!"
        name = raw_input("Your name > ")
        player = Player(name)

        with open('./.playerdata.bpydata', 'wb') as d:
            pickle.dump(player, d)


    manager = GameManager(player)

    while True:
        choice = mainMenu()

        if choice == 1:
            call(["clear"])
            manager.play()
        elif choice == 2:
            call(["clear"])
            print(player)
            raw_input()
            call(["clear"])
        elif choice == 3:
            player.setupPlayer()
            manager.updatePlayer(player)
        else:
            player.save()
            break


if __name__ == "__main__":
    main()
