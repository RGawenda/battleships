
class Grid_element:
    def __init__(self, x, y):
        self.status = 0
        self.x = x
        self.y = y
        pass

    def get_status(self):
        return self.status
        pass

    def get_x(self):
        return self.x
        pass

    def get_y(self):
        return self.y
        pass

    def change_status(self):
        self.status = self.status + 2
        pass

class Game_board:
    def __init__(self):
        matrix = []
        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                x1 = (j * 50) + 100 + j
                y1 = (i * 50) + 100 + i
                row.append(Grid_element(x1, y1))
            matrix.append(row)
        self.matrix = matrix
        pass

    def get_object(self, x, y):
        return self.matrix[x][y]
        pass

class Test_click:
    def __init__(self, board, pos):
        x, y = pos
        for k in range(0, 10):
            for l in range(0, 10):
                x1 = board.get_object(k, l).get_x()
                y1 = board.get_object(k, l).get_y()
                if ( x1 < x and x < x1+50 and y1 < y and y < y1+50):
                    if (board.get_object(k, l).get_status() < 2):
                        board.get_object(k, l).change_status()
        pass
