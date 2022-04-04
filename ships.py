

class Ship:
    def __init__(self, x, y, long):
        self.long = long
        self.x = x
        self.y = y
        pass

    def get_long(self):
        return self.long
        pass

class Carrier (Ship):
    def __init__(self, x, y, long):
        super().__init__(x, y, long)
        self.long = 5


class Battleship (Ship):
    def __init__(self, x, y, long):
        super().__init__(x, y, long)
        self.long = 4


class Destroyer	 (Ship):
    def __init__(self, x, y, long):
        super().__init__(x, y, long)
        self.long = 3

class Submarine	 (Ship):
    def __init__(self, x, y, long):
        super().__init__(x, y, long)
        self.long = 3


class Patrol_Boat (Ship):
    def __init__(self, x, y, long):
        super().__init__(x, y, long)
        self.long = 2
