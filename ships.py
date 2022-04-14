from enum import Enum


class Direction(Enum):
    direction_N = 1
    direction_E = 2
    direction_S = 3
    direction_W = 4
    pass

class Ship:
    def __init__(self, x, y, long, direction):
        self.long = long
        self.x = x
        self.y = y
        self.direction = direction
        pass

    def get_long(self):
        return self.long
        pass

class Carrier (Ship):
    def __init__(self, x, y, long, direction):
        super().__init__(x, y, long, direction)
        self.long = 5
        pass

class Battleship (Ship):
    def __init__(self, x, y, long, direction):
        super().__init__(x, y, long, direction)
        self.long = 4
        pass

class Destroyer	 (Ship):
    def __init__(self, x, y, long, direction):
        super().__init__(x, y, long, direction)
        self.long = 3
        pass

class Submarine	 (Ship):
    def __init__(self, x, y, long, direction):
        super().__init__(x, y, long, direction)
        self.long = 3
        pass

class Patrol_Boat (Ship):
    def __init__(self, x, y, long, direction):
        super().__init__(x, y, long, direction)
        self.long = 2
        pass