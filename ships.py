

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

    def get_x(self):
        return self.x
        pass

    def get_y(self):
        return self.y
        pass

    def set_x(self, x):
        self.x = x
        pass

    def set_y(self, y):
        self.y = y
        pass

    def set_direction(self, direction):
        self.direction = direction
        pass

    def get_direction(self):
        return self.direction
        pass

class Carrier(Ship):
    def __init__(self, x, y, direction):
        long = 5
        super().__init__(x, y, long, direction)
        pass


class Battleship(Ship):
    def __init__(self, x, y, direction):
        long = 4
        super().__init__(x, y, long, direction)
        pass


class Destroyer(Ship):
    def __init__(self, x, y, direction):
        long = 3
        super().__init__(x, y, long, direction)
        pass


class Submarine(Ship):
    def __init__(self, x, y, direction):
        long = 3
        super().__init__(x, y, long, direction)
        pass


class Patrol_Boat(Ship):
    def __init__(self, x, y, direction):
        long = 2
        super().__init__(x, y, long, direction)
        pass
