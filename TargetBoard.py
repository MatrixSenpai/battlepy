from Ship import Ship
from Colors import bcolors

class TargetBoard:
    board = []
    ships = []

    def __init__(self, ships):
        self.ships = ships
        self.board = {
                "A": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                "B": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                "C": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                "D": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                "E": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                "F": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                "G": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                "H": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                "I": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                "J": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
                }

    def __str__(self):
        rtr = ""
        rtr += "+  01 02 03 04 05 06 07 08 09 10 +\n"

        for (title, row) in sorted(self.board.items()):
            rtr += "%s " % title
            for place in row:
                if place == 0:
                    rtr += " o "
                elif place == 1:
                    rtr += bcolors.OKGREEN + " i " + bcolors.ENDC
                elif place == 2:
                    rtr += bcolors.FAIL + " X " + bcolors.ENDC
            rtr += " |\n"

        rtr += "+ " + "-- " * 10 + " +"

        return rtr

    def opponentTargeted(self, letter, number, wasHit):
        letter = letter.upper()
        number = int(number)
        if wasHit:
            self.board[letter][number] = 2
        else:
            self.board[letter][number] = 1

        print self.board[letter][number]
