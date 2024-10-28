class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])
        self.obstacle_grid = obstacleGrid
        self.stored_unique_paths = [[-1 for c in range(n)] for r in range(m)]
        res = self.unique_paths_ii_from_position(0, 0)
        return res

    def unique_paths_ii_from_position(self, row, column):
        if row >= self.m:
            raise Exception(f"Invalid row {row}")
        if column >= self.n:
            raise Exception(f"Invalid row {column}")
        if row == self.m - 1 and column == self.n - 1:
            # Ensure to store the value when it's the last square
            self.stored_unique_paths[row][column] = 1

        if self.stored_unique_paths[row][column] != -1:
            return self.stored_unique_paths[row][column]

        unique_paths = 0
        if row + 1 < self.m:
            if self.stored_unique_paths[row + 1][column] != -1:
                unique_paths += self.stored_unique_paths[row + 1][column]
            else:
                unique_paths += self.unique_paths_from_position(row + 1, column)
        if column + 1 < self.n:
            if self.stored_unique_paths[row][column + 1] != -1:
                unique_paths += self.stored_unique_paths[row][column + 1]
            else:
                unique_paths += self.unique_paths_from_position(row, column + 1)
        self.stored_unique_paths[row][column] = unique_paths
        return unique_paths
