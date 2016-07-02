class Ship:
    name = ""
    size = 0
    health = 0
    places = []
    location = []

    def __init__(self, size, place):
        self.size = size
        self.health = size

        if size == 2:
            self.name = "Destroyer"
        elif size == 3:
            self.name = "Cruiser"
        elif size == 4:
            self.name = "Battleship"
        else:
            self.name = "Carrier"

        self.places = []
        for i in range(size):
            self.places.append(0)

        self.location = place

    def __str__(self):
        rtr = ""
        rtr += "%s\n <|" % self.name
        for c in self.places:
            if c == 0:
                rtr += " O |"
            else:
                rtr += " X |"
        rtr += ">\n"
        rtr += self.location.__str__() + "\n"

        return rtr

