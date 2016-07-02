class Player:
    name = ""
    wins = 0
    losses = 0
    level = 1
    isComputer = False

    targetBoard = ""
    placeBoard = ""

    def __init__(self):
        self.name = "Computer"

    def __str__(self):
        winper = 0
        if self.losses == 0 and self.wins > 0:
            winper = 100
        if self.losses > 0:
            winper = (self.wins/self.lossess) * 100

        rtr = ""

        rtr += "%s (Level %d)\n" % (self.name, self.level)
        rtr += "Wins:            %d\n" % self.wins
        rtr += "Losses:          %d\n" % self.losses
        rtr += "Win Percentage:  %d%%\n" % winper

        return rtr

    def placeShips(self):
        self.placeBoard = PlayerBoard()
        self.placeBoard.compBoard()

        ships = self.placeBoard.ships
        self.targetBoard = TargetBoard(ships)

    def setName(self, newName):
        self.name = newName

    def save(self):
        with open(playerDataFile, 'wb') as d:
            pickle.dump(self, d)

    def setupPlayer(self):
        n = raw_input("Enter your name > ")
        self.name = n
        self.save()
