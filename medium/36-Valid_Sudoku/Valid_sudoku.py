from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        set_cols_arr = [
            set(), set(), set(),
            set(), set(), set(),
            set(), set(), set()
        ]
        set_3x3_arr = [
            [set(), set(), set()],
            [set(), set(), set()],
            [set(), set(), set()]
        ]
        current_row_set = set()

        for row in range(9):

            current_row_set.clear()

            # Iterate over each item of each row
            for col in range(9):

                item = board[row][col]
                if item == '.': continue # If the item is a '.' continue.

                # If its in the same row, return false
                if item in current_row_set:
                    return False

                # If the item is already in the column, return false
                if item in set_cols_arr[col]:
                    return False

                # Then we have to compute in which 3x3 grid it is and check if its there    
                # To compute that we use mod operators
                if item in set_3x3_arr[row //3][col // 3]:
                    return False
                
                # Add the items to the sets if everything passed
                set_cols_arr[col].add(item)
                current_row_set.add(item)
                set_3x3_arr[row // 3][col // 3].add(item)

        return True