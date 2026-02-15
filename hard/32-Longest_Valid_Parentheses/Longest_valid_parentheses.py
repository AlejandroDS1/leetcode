class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # In this stack will be the indices of the start of the substring
        max_len = 0

        for i in range(len(s)):
            if s[i] == "(": # If there is a posibility of start of substring, add it to the stack
                stack.append(i)
            else:
                stack.pop() # If we are closing a substring, pop it from the stack
                
                # If there aren't more indexes in the stack
                # We add it to have the index of the last closing one
                # This closing one acts as a "end of possible substrings"
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len 