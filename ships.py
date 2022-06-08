

class Ship:
    def __init__(self, x, y, long, direction):
        self.long = long
        self.x = x
        self.y = y
        self.direction = direction

    def get_long(self):
        return self.long

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction


class Carrier(Ship):
    def __init__(self, x, y, direction):
        long = 5
        super().__init__(x, y, long, direction)


class Battleship(Ship):
    def __init__(self, x, y, direction):
        long = 4
        super().__init__(x, y, long, direction)
        pass


class Destroyer(Ship):
    def __init__(self, x, y, direction):
        long = 3
        super().__init__(x, y, long, direction)


class Submarine(Ship):
    def __init__(self, x, y, direction):
        long = 3
        super().__init__(x, y, long, direction)


class PatrolBoat(Ship):
    def __init__(self, x, y, direction):
        long = 2
        super().__init__(x, y, long, direction)
