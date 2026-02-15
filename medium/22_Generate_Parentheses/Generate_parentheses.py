from typing import List
class Solution:

    def next_step(self, current_string, open_parentheses, parentheses_left):
        """
            params:
                current_string : str The current string this branch is computing, at this point

        """

        if parentheses_left == 0:
            self.RESULT_LIST.append(current_string)
            return

        # If there is no open parentheses. We can only open one more
        if open_parentheses == 0:
            return self.next_step(current_string + '(', 1, parentheses_left)

        # If there are open parentheses and we still can open more of them. We do
        if (parentheses_left - open_parentheses) > 0:
            self.next_step(current_string + '(', open_parentheses + 1, parentheses_left)

        if open_parentheses > 0:
            self.next_step(current_string + ')', open_parentheses - 1, parentheses_left - 1)
        

    def generateParenthesis(self, n: int) -> List[str]:

        self.n = n

        self.RESULT_LIST = []

        self.next_step(current_string='(', 
                       open_parentheses=1,
                       parentheses_left=n)


        return self.RESULT_LIST
    
print(Solution().generateParenthesis(18))