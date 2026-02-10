class Spreadsheet:

    def __init__(self, rows: int):
        
        self.grid = self.grid = [[0]*26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        
        x, y = self.cell_decode(cell)
        self.grid[x][y] = value

    def resetCell(self, cell: str) -> None:
        x, y = self.cell_decode(cell)
        self.grid[x][y] = 0 

    def getValue(self, formula: str) -> int:

        def check_type(o: str) -> int:
            try:
                int(o[0])
                return int(o)
            except ValueError:
                x, y = self.cell_decode(o)
                return self.grid[x][y]
            

        first, second = formula[1:].split("+")
        
        # Check if one operand is a cell or a number
        first, second = check_type(first), check_type(second)

        return first + second

    def cell_decode(self, cell : str) -> tuple:
        
        y = ord(cell[0]) - 65
        x = int(cell[1:]) - 1
        return (x, y)