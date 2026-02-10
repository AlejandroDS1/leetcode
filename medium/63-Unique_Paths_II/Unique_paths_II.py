from collections import List

class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[m - 1][n - 1] == 1: return 0

        grid = [[0 for y in range(n)] for x in range(m)]

        grid[0][0] = 1

        # Iterate over the cells and sum the only adjacent ones
        for x in range(m):
            for y in range(n):
                
                # Sum the adjacent cells to the cell if the adjacents exists 
                if ((x - 1) >= 0) and (obstacleGrid[x-1][y] == 0):
                    grid[x][y] += grid[x-1][y]
                if ((y - 1) >= 0) and (obstacleGrid[x][y-1] == 0):
                    grid[x][y] += grid[x][y-1]


        return grid[m-1][n-1]