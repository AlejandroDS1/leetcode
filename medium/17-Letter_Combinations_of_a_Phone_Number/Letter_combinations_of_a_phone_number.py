from typing import List
class Solution:

    def __init__(self):
        self.MAP_DIGITS = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def nextLetter(self, current_string = '', digit_position = 0):
        
        """
        Recursive function to find all strings.
        """

        for letter in self.MAP_DIGITS[self.digits[digit_position]]:
            new_string = current_string + letter

            # Base case were we found the full string to add
            if digit_position == (len(self.digits) - 1):
                self.list_of_combinations.append(new_string)
            else:
                self.nextLetter(new_string, digit_position + 1)

        
        
    def letterCombinations(self, digits: str) -> List[str]:

        self.digits = digits

        if len(digits) == 1: return list(self.MAP_DIGITS[digits[0]])

        self.list_of_combinations = []

        self.nextLetter('', digit_position = 0)
        return self.list_of_combinations