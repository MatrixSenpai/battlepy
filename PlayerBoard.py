from subprocess import call
from Colors import bcolors
from Ship import Ship

gridLength = 10
gridHeight = 10
gridNum = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J"}

class PlayerBoard:
    board = []
    ships = []

    # Note
    # Board:
        # 0: No ship, not fired
        # 1: No ship, miss
        # 2: Ship, not fired
        # 3: Ship, hit
    def __init__(self):
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

    def compBoard(self):
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
        carrierCells = ["A2", "B2", "C2", "D2", "E2"]
        self.updateBoard(carrierCells)
        carrier = Ship(5, carrierCells)
        battleCells = ["D5", "D6", "D7", "D8"]
        self.updateBoard(battleCells)
        battle = Ship(4, battleCells)
        cruiserOCells = ["F6", "G6", "H6"]
        self.updateBoard(cruiserOCells)
        cruiserOne = Ship(3, cruiserOCells)
        cruiserTCells = ["I2", "I3", "I4"]
        self.updateBoard(cruiserTCells)
        cruiserTwo = Ship(3, cruiserTCells)
        destroyCells = ["A7", "B7"]
        self.updateBoard(destroyCells)
        destroyer = Ship(2, destroyCells)

        self.ships = [carrier, battle, cruiserOne, cruiserTwo, destroyer]

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
                    rtr += bcolors.WARNING + " o " + bcolors.ENDC
                elif place == 3:
                    rtr += bcolors.FAIL + " X " + bcolors.ENDC
            rtr += " |\n"

        rtr += "+ " + "-- " * 10 + " +"
        return rtr

    def placeShips(self):
        call(["clear"])
        num = [5, 4, 3, 3, 2]
        r = True
        for s in num:
            print(self)
            while r:
                if s == 2:
                    t = "Destroyer"
                elif s == 3:
                    t = "Cruiser"
                elif s == 4:
                    t = "Battleship"
                else:
                    t = "Carrier"
                print("\nPlace your %s" % t)

                user = raw_input("Enter letter & number of first place > ")
                (frow, fnum) = list(user)
                align = raw_input("Vertical or Horizontal [H/v]> ")

                frow = frow.upper()
                fnum = int(fnum)

                cells = []

                if align.lower() == "" or align.lower() == "h":
                    # Ships are horizontal
                    final = fnum + s

                    if final > gridLength:
                        print("Illegal entry! %s is too long to fit there!" % t)
                        continue

                    i = fnum
                    while i < final:
                        cells.append("%s%d" % (frow, i))
                        i += 1
                else:
                    # Ships are vertical
                    start = 0
                    data = sorted(gridNum.items())
                    for (k, l) in data:
                        if l == frow:
                            start = k - 1

                    final = start + s

                    if final > gridHeight:
                        print("Illegal entry! %s is too tall to fit there!" % t)
                        continue

                    for (k, l) in data[start:final]:
                        cells.append("%s%d" % (l, fnum))

                newShip = Ship(s, cells)

                if self.updateBoard(cells):
                    self.ships.append(newShip)
                    call(["clear"])
                    break

    def updateBoard(self, cells):
        for cell in cells:
            (letter, number) = list(cell)
            number = int(number) - 1
            place = self.board[letter][number]

            if place == 2:
                print("%s%d is already taken! Please try again!" % (letter, number))
                return False
            else:
                self.board[letter][number] = 2

        return True

    def guess(self, letter, number):
        l = letter.upper()
        n = int(number) - 1
        data = self.board[l][n]
        if data == 0:
            print("%s%s, Miss!" % (l, number))
            self.board[l][n] = 1
            return False
        if data == 2:
            print("%s%s, Hit!" % (l, number))
            self.board[l][n] = 3

            for ship in self.ships:
                for place in ship.location:
                    if place == "%s%s" % (letter.upper(), number):
                        ship.health = ship.health - 1
                        if ship.health == 0:
                            print "%s is sunk!" % ship.name
            return True
        if data == 1 or data == 3:
            print("%s%s, Already targeted!" % (l, number))
            return "x"

    def getHealth(self):
        for ship in self.ships:
            if ship.health > 0:
                return True
        return False
