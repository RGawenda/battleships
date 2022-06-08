

class GridElement:
    def __init__(self, x, y):
        self.status = 0
        self.x = x
        self.y = y

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

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


class GridStructure:
    def __init__(self):
        matrix = []
        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                x1 = (i * 50) + 100 + i
                y1 = (j * 50) + 100 + j
                row.append(GridElement(x1, y1))
            matrix.append(row)
        self.matrix = matrix
        pass

    def get_object(self, x, y):
        return self.matrix[x][y]

    def import_grid(self, grid):
        for x in range(0, 10):
            for y in range(0, 10):
                self.matrix[x][y].set_status(grid[x][y])
