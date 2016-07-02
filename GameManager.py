import json
import random
import pickle
from time import sleep
from subprocess import call
from PlayerBoard import PlayerBoard
from TargetBoard import TargetBoard
from Player import Player

managerDataFile = "./.manager.bpydata"

class GameManager:

    humPlayer = ""
    humPlaceBoard = ""
    humTargetBoard = ""

    comPlayer = ""
    comPlaceBoard = ""
    comTargetBoard = ""

    turn = True

    def __init__(self, player):
        self.humPlayer = player
        self.humPlaceBoard = PlayerBoard()

        self.comPlayer = Player("Computer")
        self.comPlaceBoard = PlayerBoard()
        self.comPlaceBoard.compBoard()

    def updatePlayer(self, newPlayer):
        self.humPlayer = newPlayer

    def save(self):
        with open(managerDataFile, 'wb') as d:
            pickle.dump(self, d)

    def play(self):
        turn = True

        self.humPlayer.placeShips()
        self.comPlayer.placeShips()

        # 2. Start Playing
        while True:
            if turn:
                # Player's turn
                target = self.humPlayer.turn()
                l = ""
                n = ""
                if len(target) != 2:
                    l = target[0]
                    n = 10
                else:
                    (l, n) = list(target)

                res = self.comPlayer.targeted(l, n)
                if res:
                    self.humPlayer.hit(l, n)
                else:
                    self.humPlayer.miss(l, n)

            else:
                # Computer's turn
                self.displayBoard(self.comTargetBoard, self.comPlaceBoard, True)
                print "Computer targeting..."
                sleep(2)
                l = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "J", "I"])
                n = random.randint(1, 9)
                res = self.humPlaceBoard.guess(l, n)
                if res == "x":
                    continue
                self.comTargetBoard.opponentTargeted(l, n, res)
                self.displayBoard(self.comTargetBoard, self.comPlaceBoard, True)
                turn = True
                sleep(2)

            hh = self.humPlaceBoard.getHealth()
            ch = self.comPlaceBoard.getHealth()

            if not hh:
                self.humPlayer.losses = self.humPlayer.losses + 1
                print "Computer Wins!"
                break
            if not ch:
                self.humPlayer.wins = self.humPlayer.wins + 1
                print "Player Wins!"
                break
            call(["clear"])

    def displayBoard(self, target, place, comp):
        print target
        if not comp:
            print place
