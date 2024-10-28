class Game:
    def __init__(self, n, m):
        self.m = m
        self.n = n

    def unique_paths_from_position(self, row, column):
        if row > self.m:
            raise Exception(f"Invalid row {row}")
        if column > self.n:
            raise Exception(f"Invalid row {column}")
        if row == self.m and column == self.n:
            return 1

        unique_paths = 0
        if row + 1 <= self.m:
            unique_paths += self.unique_paths_from_position(row + 1, column)
        if column + 1 <= self.n:
            unique_paths += self.unique_paths_from_position(row, column + 1)
        return unique_paths
