class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        # Create grid of m x n to store the amount of paths at each cell
        grid = [[0 for y in range(n)] for x in range(m)]        

        grid[0][0] = 1 # Make the first one 1 to sum

        # Iterate over the cells and sum the only adjacent ones
        for x in range(m):
            for y in range(n):
                
                # Sum the adjacent cells to the cell if the adjacents exists 
                if (x - 1) > 0: grid[x][y] += grid[x-1][y]
                if (y - 1) > 0: grid[x][y] += grid[x][y-1]


        return grid[m-1][n-1]