import json
from grid import GridStructure


class JsonFileHandler:

    def save(self, grid_data: GridStructure, grid2_data: GridStructure, turn: bool, mode: bool, path):
        grid = []
        grid2 = []
        for i in range(0, 10):
            row = []
            row2 = []
            for j in range(0, 10):
                row.append(grid_data.get_object(i, j).get_status())
                row2.append(grid2_data.get_object(i, j).get_status())
            grid.append(row)
            grid2.append(row2)

        json_save_data = {"player grid": grid,
                          "enemy grid": grid2,
                          "turn": turn,
                          "mode": mode}

        with open(path, "w") as write_file:
            json.dump(json_save_data, write_file)

    def load(self, path):
        with open(path) as json_file:
            data = json.load(json_file)
            return data


class TextFileHandler:

    def save(self, grid_data: GridStructure, grid2_data: GridStructure, turn: bool, mode: bool, path):
        with open(path, "w") as write_file:

            grid = []
            grid2 = []
            for i in range(0, 10):
                row = []
                row2 = []
                for j in range(0, 10):
                    row.append(grid_data.get_object(i, j).get_status())
                    row2.append(grid2_data.get_object(i, j).get_status())
                grid.append(row)
                grid2.append(row2)
            for row in grid:
                write_file.writelines(','.join(str(status) for status in row))
                write_file.writelines('\n')
            for row2 in grid2:
                write_file.writelines((','.join(str(status) for status in row2)))
                write_file.writelines('\n')
            write_file.writelines(str(turn))
            write_file.writelines('\n')
            write_file.writelines(str(mode))
            write_file.writelines('\n')


    def load(self, path):
        with open(path) as file:

            lines = file.readlines()

            grid = []
            grid2 = []
            for i in range(0, 10):
                grid.append(lines[0].split(","))
                for j in range(0, len(grid[i])):
                    grid[i][j] = int(grid[i][j])
                lines.pop(0)
            for i in range(0, 10):
                grid2.append(lines[0].split(","))
                for j in range(0, len(grid[i])):
                    grid2[i][j] = int(grid2[i][j])
                lines.pop(0)
            if "True" in lines[0]:
                turn = True
            else:
                turn = False
            lines.pop(0)
            if "True" in lines[0]:
                mode = True
            else:
                mode = False

            data = {"player grid": grid,
                    "enemy grid": grid2,
                    "turn": turn,
                    "mode": mode}

            return data
