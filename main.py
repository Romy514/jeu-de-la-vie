from copy import copy, deepcopy


class JeuDeLaVie:

    def __init__(self):
        self.grid = [[0 for i in range(0, 3)] for i in range(0, 3)]

    def get_grid(self):
        return self.grid

    def print_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end=" ")
            print('\n------')

    def add_cell(self, row, col):
        self.grid[row][col] = 1

    def remove_cell(self, row, col):
        self.grid[row][col] = 0

    def check_neighbours(self, row, col):
        neighbour_count = 0
        rows, cols = len(self.grid), len(self.grid[0])

        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols:
                    if self.grid[r][c]:
                        neighbour_count += 1
        return neighbour_count

    def iteration(self):
        new_grid = deepcopy(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                neighbours = self.check_neighbours(i, j)

                if self.grid[i][j] == 1:
                    if neighbours < 2:
                        new_grid[i][j] = 0
                    elif neighbours > 3:
                        new_grid[i][j] = 0
                    else:
                        continue

                elif self.grid[i][j] == 0:
                    if neighbours == 3:
                        new_grid[i][j] = 1
                    else:
                        continue

        self.grid = new_grid

    def iterate(self, iterations):
        for i in range(iterations):
            self.iteration()
