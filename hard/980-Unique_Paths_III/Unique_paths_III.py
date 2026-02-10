class Solution:

    def find_properties(self, grid: List[List[int]]):

        self.start_point = (0,0)
        
        self.n_obstacles = 0

        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j]  == 1: self.start_point = (i, j)
                if  grid[i][j] == -1: self.n_obstacles += 1


    def find_path(self, grid: List[List[int]], current_path: List[tuple], set_current_path: Set[tuple]):
        
        x, y = current_path[-1] # current_path[-2] is where we come from
        
        current_value = grid[x][y]

        # TODO: if end but not needed_squares return

        if (x, y) in set_current_path:
            return

        elif (current_value == 2) and (len(current_path) == self.needed_squares):

            self.paths.append(current_path)
        
        # When current_value == -1 we will return the function ending recursivity

        elif (current_value == 0) or (current_value == 1):
            # Logic to take another step
            for x0, y0 in self.directions:

                nx = x + x0
                if (nx < 0) or (nx > len(grid) - 1): continue

                ny = y + y0
                if (ny < 0) or (ny > len(grid[0]) - 1): continue

                new_current_path = current_path + [(nx, ny)]
                self.find_path(grid, new_current_path, set(current_path))
        return

            
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        '''
            1 representing the starting square. There is exactly one starting square.
            2 representing the ending square. There is exactly one ending square.
            0 representing empty squares we can walk over.
            -1 representing obstacles that we cannot walk over.
        ''' 
        
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        self.find_properties(grid)

        self.needed_squares = len(grid) * len(grid[0]) - self.n_obstacles
        
        self.paths = []

        self.find_path(grid, [self.start_point], set())

        return len(self.paths)