

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
        pass

class Battleship (Ship):
    def __init__(self, x, y, long):
        super().__init__(x, y, long)
        self.long = 4
        pass

class Destroyer	 (Ship):
    def __init__(self, x, y, long):
        super().__init__(x, y, long)
        self.long = 3
        pass

class Submarine	 (Ship):
    def __init__(self, x, y, long):
        super().__init__(x, y, long)
        self.long = 3
        pass

class Patrol_Boat (Ship):
    def __init__(self, x, y, long):
        super().__init__(x, y, long)
        self.long = 2
        pass