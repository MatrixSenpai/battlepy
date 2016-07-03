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

    comPlayer = ""

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

        l = ""
        n = ""
        while True:
            if turn:
                # Player's turn
                target = self.humPlayer.turn()
                (l, n) = self.evalTarget(target)

                res = self.comPlayer.targeted(l, n)
                if res:
                    self.humPlayer.hit(l, n)
                else:
                    self.humPlayer.miss(l, n)

                sleep(3)
            else:
                # Computer's turn
                target = self.comPlayer.turn()
                (l, n) = self.evalTarget(target)

                res = self.humPlayer.targeted(l, n)
                if res == True:
                    self.comPlayer.hit(l, n)
                elif res == False:
                    self.comPlayer.miss(l, n)
                else:
                    continue

                turn = True

            hh = self.humPlayer.health()
            ch = self.comPlayer.health()

            if not hh:
                self.humPlayer.losses = self.humPlayer.losses + 1
                self.humPlayer.save()
                print "Computer Wins!"
                break
            if not ch:
                self.humPlayer.wins = self.humPlayer.wins + 1
                self.humPlayer.save()
                print "Player Wins!"
                break
            call(["clear"])

    def evalTarget(self, target):
        l = ""
        n = 0
        if len(target) != 2:
            l = target[0]
            n = 10
        else:
            (l, n) = list(target)

        return (l, n)

    def displayBoard(self, target, place, comp):
        print target
        if not comp:
            print place
