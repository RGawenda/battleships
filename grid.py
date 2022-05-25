

class Grid_element:
    def __init__(self, x, y):
        self.status = 0
        self.x = x
        self.y = y

    def get_status(self):
        return self.status

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_ship(self):
        self.status = 1

    def remove_ship(self):
        self.status = 0

    def change_status(self):
        self.status = self.status + 2


class Grid_structure:
    def __init__(self):
        matrix = []
        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                x1 = (i * 50) + 100 + i
                y1 = (j * 50) + 100 + j
                row.append(Grid_element(x1, y1))
            matrix.append(row)
        self.matrix = matrix
        pass

    def get_object(self, x, y):
        return self.matrix[x][y]